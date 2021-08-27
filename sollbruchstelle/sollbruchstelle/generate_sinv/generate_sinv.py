import frappe
from datetime import date
from datetime import timedelta
from datetime import datetime
from frappe.utils.data import today, add_days, date_diff

@frappe.whitelist()
def generate_sinv(doc):

    mietvertrag = frappe.get_doc('Mietvertrag', doc)
    ges_object = frappe.get_doc('Gesamtobjekt', mietvertrag.total_object)
    
    date1 = mietvertrag.contract_start
    date2 = mietvertrag.contract_end
    
    date_delta = date2 - date1

    days = date_delta.days / 7
    months = days / 4
    #rest = days % 4
    
    day_diff = date_diff(mietvertrag.contract_start, today())
    
    if day_diff >= 30:
        due_date = mietvertrag.contract_start - timedelta(days=30)
    else:
        due_date = mietvertrag.contract_start - timedelta(days=day_diff)
    print(due_date)
    sinv = frappe.get_doc({
        'doctype': 'Sales Invoice',
        'customer': mietvertrag.customer,
        'due_date': due_date,
        'supplier_group': "All Supplier Groups",
        'mietvertrag': mietvertrag.name
    })
    
    for i in mietvertrag.mietobjekte:
        row = sinv.append("items", {})
        row.item_code = "M000"
        row.item_name = i.object_name
        row.qty = int(months)
        row.rate = i.rate
        
        # second_row = sinv.append("items", {})
        # second_row.item_code = "M000"
        # second_row.item_name = "Halber Monat: " + i.object_name
        # second_row.qty = 1
        # second_row.rate = i.rate / 2
        
        
    if mietvertrag.setup_fee:
        third_row = sinv.append("items", {})
        third_row.item_code = "A000"
        third_row.item_name = "Aufschaltgebühr"
        third_row.qty = 1
        third_row.rate = mietvertrag.setup_fee
        
    print(sinv.grand_total)
    sinv.insert()
    return 
