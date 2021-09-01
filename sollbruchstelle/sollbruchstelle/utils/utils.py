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

#@frappe.whitelist()
#def create_nachtrag(total_object, contract_start, contract_end):
#    mietvertrag = frappe.get_doc({
#        "doctype": "Mietvertrag",
#        "contract_type": "Nachtrag",
#        "contract_start": contract_start,
#        "contract_end": contract_end
#    })
#    mietvertrag.insert()                                    
#    
#    return mietvertrag.name

# def get_contracts():
    # #get all contracts for selected total_object
    # sql_query = """SELECT FROM `tabMietvertrag` WHERE `tabMietvertrag`.`total_object` = {total_object} AND `tabMietvertrag`.`docstatus` = 2
    # ;"""
    # frappe.db.sql(sql_query, as dict=1)
    # return
