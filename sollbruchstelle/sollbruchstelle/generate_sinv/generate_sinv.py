import frappe
from datetime import date
from datetime import timedelta
from datetime import datetime

@frappe.whitelist()
def generate_sinv(doc):

    mietvertrag = frappe.get_doc('Mietvertrag', doc)
    ges_object = frappe.get_doc('Gesamtobjekt', mietvertrag.total_object)
    sinv = frappe.new_doc("Sales Invoice")
    sinv.customer = mietvertrag.customer
    sinv.due_date = mietvertrag.contract_start - timedelta(days=30)
    sinv.supplier_group = "All Supplier Groups"
    sinv.global_id = "32"
    
    date1 = mietvertrag.contract_start
    date2 = mietvertrag.contract_end
    
    date_delta = date1 - date2

    days = date_delta.days / 7
    months = days / 4
    rest = days % 4
    
    for i in mietvertrag.mietobjekte:
        row = sinv.append("items", {
                "item_code": "M000",
                "item_name": i.object_name, 
                "qty": int(months),
                "rate": i.rate,
            })
		
        row = sinv.append("items", {
                "item_code": "M000",
                "item_name": "Halber Monat: " + i.object_name, 
                "qty": 1,
                "rate": i.rate / 2,
            })
        
        
    if mietvertrag.posting_fee:
        row2= sinv.append("items", {
            "item_code": "A000",
            "item_name": "Aufschaltgebühr",
            "qty": 1,
            "rate": mietvertrag.posting_fee,
        })  
        
    sinv.save()
    return #sinv.naming_series
