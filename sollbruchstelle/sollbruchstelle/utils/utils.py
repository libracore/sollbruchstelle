# -*- coding: utf-8 -*-
# Copyright (c) 2021, Libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def cleanup_contacts():
    dublicate_contacts = frappe.db.sql("""SELECT `user`, COUNT(*) FROM `tabContact` WHERE `user` IS NOT NULL GROUP BY `user` HAVING COUNT(*) > 1""", as_dict=True)
    
    for duplicate_contact in dublicate_contacts:
        contacts = frappe.db.sql("""SELECT `name` FROM `tabContact` WHERE `user` = '{user}' ORDER BY `creation` ASC""".format(user=duplicate_contact.user), as_dict=True)
        qty = len(contacts)
        loop = 1
        for _contact in contacts:
            if loop < qty:
                contact = frappe.get_doc("Contact", _contact.name)
                contact.delete()
                loop += 1

@frappe.whitelist()
def create_nachtrag(total_object, contract_start, contract_end, notice_period, old_contract_end):

    whgen = frappe.get_all('Mietobjekt',
        filters={
            'total_object': total_object
        },
        fields=['name'])
    for whg in whgen:
        mietvertraege = frappe.get_all('Mietvertrag', ["name"],
        filters={
            'object_name': whg.name,
            'docstatus': 1
        },
        order_by="creation desc", limit_page_length=1)
        if len(mietvertraege) > 0:
            mietvertrag = frappe.get_doc("Mietvertrag", mietvertraege[0]["name"])
            #only create if ungekuendigt
            kuendigungen = frappe.get_all("Kuendigung", ["name"],
            filters={
                'mietvertrag': mietvertrag.name,
                'docstatus': 1
            })
            if len(kuendigungen) == 0:
                nachtrag = frappe.get_doc(frappe.copy_doc(mietvertrag))
                nachtrag.contract_type = 'Nachtrag'
                nachtrag.contract_start = contract_start
                nachtrag.contract_end = contract_end
                nachtrag.notice_period = notice_period
                nachtrag.old_contract_end = old_contract_end
                nachtrag.nachtrag_nr = len(mietvertraege)
                nachtrag.naming_series = 'NM-.#####'
                #linkfield to mietvertrag
                nachtrag.mietvertrag = mietvertrag.name
                try:
                    nachtrag.insert()
                except Exception as err:
                    frappe.log_error("Unable to create {0} ({1})".format(nachtrag.as_dict(), err), "Nachtrag erstellen fehlgeschlagen")
                try:
                    mietvertrag.replaced = 1
                    mietvertrag.save()
                except Exception as err:
                    frappe.log_error("Unable to create {0} ({1})".format(mietvertrag.as_dict(), err), "Mietvertrag Updatefehlgeschlagen") 
    return                                
