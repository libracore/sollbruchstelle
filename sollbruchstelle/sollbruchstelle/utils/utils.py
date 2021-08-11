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
