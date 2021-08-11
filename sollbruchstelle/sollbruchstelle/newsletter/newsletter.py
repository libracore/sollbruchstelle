# -*- coding: utf-8 -*-
# Copyright (c) 2021, Libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_subscribers(total_object, email_group):
    emails = get_emails(total_object)
    qty, duplicate = create_email_group_members(emails, email_group)
    return {
        'qty': qty,
        'duplicate': duplicate
    }

def get_emails(total_object):
    emails = get_mietobjekte(total_object)
    return emails
    
def get_mietobjekte(total_object):
    mietobjekte = frappe.db.sql("""SELECT `name` FROM `tabMietobjekt` WHERE `total_object` = '{total_object}'""".format(total_object=total_object), as_dict=True)
    if len(mietobjekte) > 0:
        emails = get_vertraege(mietobjekte)
        return emails
    else:
        return []
        
def get_vertraege(mietobjekte):
    emails = []
    for mietobjekt in mietobjekte:
        object_name = mietobjekt.name
        vertraege = frappe.db.sql("""SELECT `customer` FROM `tabMietvertrag` WHERE `object_name` = '{object_name}'""".format(object_name=object_name), as_dict=True)
        for vertrag in vertraege:
            contacts = frappe.db.sql("""
                                        SELECT `email_id`
                                        FROM `tabContact`
                                        WHERE `name` IN (
                                            SELECT `parent`
                                            FROM `tabDynamic Link`
                                            WHERE `parenttype` = 'Contact'
                                            AND `link_doctype` = 'Customer'
                                            AND `link_name` = '{customer}'
                                        )""".format(customer=vertrag.customer), as_dict=True)
            for contact in contacts:
                if contact.email_id:
                    emails.append(contact.email_id)
    return emails
    
def create_email_group_members(emails, email_group):
    qty = 0
    duplicate = 0
    for email in emails:
        try:
            email_group_member = frappe.get_doc({
                "doctype": "Email Group Member",
                "email_group": email_group,
                "email": email
            })
            email_group_member.insert()
            qty += 1
        except frappe.UniqueValidationError:
            frappe.local.message_log = []
            duplicate += 1
    return qty, duplicate
