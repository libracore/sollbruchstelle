# -*- coding: utf-8 -*-
# Copyright (c) 2021, libracore.com and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
'''
def submit_payment_reminder
daily, Zahlungserinnerung:
get all SI where due date (+10 tage) and keine PR dazu
create PR level 1

daily, Mahnung
get all PR where due date (+30 Tage) and keine PR level 2
create PR level 2


sql_query = ("""SELECT `name`, `due_date`, `posting_date`, `payment_reminder_level`, `grand_total`, `outstanding_amount` 
                    FROM `tabSales Invoice` 
                    WHERE `outstanding_amount` > 0 AND `customer` = '{customer}'
                      AND `docstatus` = 1
                      AND `enable_lsv` = 0
                      AND (`due_date` < CURDATE())
                      AND `company` = "{company}"
                      AND ((`exclude_from_payment_reminder_until` IS NULL) OR (`exclude_from_payment_reminder_until` < CURDATE()));
                    """.format(customer=customer.customer, company=company))
            open_invoices = frappe.db.sql(sql_query, as_dict=True)
'''
