# -*- coding: utf-8 -*-
# Copyright (c) 2021, Libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_subscribers(total_object, list_type, email_group):
    purge_email_group(email_group)
    emails = get_emails(total_object, list_type)
    qty, duplicate = create_email_group_members(emails, email_group)
    return {
        'qty': qty,
        'duplicate': duplicate
    }
    
def get_emails(total_object, list_type):
    if list_type == 'Mieter': 
        sql_query = """SELECT `contracts`.`contact`, `tabContact`.`email_id`, `contracts`.`name`, `tabKuendigung`.`name`
            FROM (
                SELECT `contact`, `name`
                FROM `tabMietvertrag` 
                WHERE `total_object` = "{total_object}"
                  AND `docstatus` = 1
                  AND `tabMietvertrag`.`replaced` = 0
                UNION SELECT `contact_2` AS `contact`, `name`
                FROM `tabMietvertrag` 
                WHERE `total_object` = "{total_object}"
                  AND `contact_2` IS NOT NULL AND `docstatus` = 1
                  AND `tabMietvertrag`.`replaced` = 0
                ) AS `contracts`
            LEFT JOIN `tabContact` ON `contracts`.`contact` = `tabContact`.`name`
            LEFT JOIN `tabKuendigung` ON `tabKuendigung`.`mietvertrag` = `contracts`.`name`
            /*entfernt gekuendigte*/
            WHERE (`tabContact`.`email_id` IS NOT NULL)
              AND `tabKuendigung`.`name` IS NULL
              AND `tabContact`.`unsubscribed` = 0  """.format(total_object = total_object)
    else: 
        if list_type == 'Mieter und Untermieter': 
            filter = "AND `tabKuendigung`.`name` IS NULL"
        else:
            filter = ""
        sql_query = """SELECT `contracts`.`customer`, `tabContact`.`email_id`, `contracts`.`name`, `tabKuendigung`.`name`
            FROM (
                SELECT `customer`, `name`
                FROM `tabMietvertrag` 
                WHERE `total_object` = "{total_object}"
                  AND `docstatus` = 1
             /*ersetzt checkbox als filter muss 0 sein*/
                UNION SELECT `customer_2` AS `customer`, `name`
                FROM `tabMietvertrag` 
                WHERE `total_object` = "{total_object}"
                  AND `customer_2` IS NOT NULL AND `docstatus` = 1
                   /*ersetzt checkbox als filter muss 0 sein*/
                ) AS `contracts`
            JOIN `tabDynamic Link` ON (`tabDynamic Link`.`link_name` = `contracts`.`customer`
                AND `tabDynamic Link`.`parenttype` = 'Contact'
                AND `tabDynamic Link`.`link_doctype` = 'Customer')
            LEFT JOIN `tabContact` ON `tabDynamic Link`.`parent` = `tabContact`.`name`
            LEFT JOIN `tabKuendigung` ON `tabKuendigung`.`mietvertrag` = `contracts`.`name`
            /*entfernt gekuendigte*/
            WHERE (`tabContact`.`email_id` IS NOT NULL)
            AND `tabContact`.`unsubscribed` = 0 {filter}""".format(total_object = total_object, filter = filter)
    
    email_data = frappe.db.sql(sql_query, as_dict=True)
    emails = []
    for row in email_data:
        if row.email_id not in emails:
            emails.append(row.email_id)
    return emails
    
def purge_email_group(email_group):
    frappe.db.sql("""DELETE FROM `tabEmail Group Member` WHERE `email_group` = "{email_group}";""".format(email_group = email_group))
    return
    
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
