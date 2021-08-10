# Copyright (c) 2021, Libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    filters = frappe._dict(filters or {})
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    return [
        {"label": _("Mietvertrag"), "fieldname": "mietvertrag", "fieldtype": "Link", 'options': 'Mietvertrag', "width": 90},
        {"label": _("Gesamtobjekt"), "fieldname": "total_object", "fieldtype": "Link", "options": "Gesamtobjekt", "width": 150},
        {"label": _("Mietobjekt"), "fieldname": "object_name", "fieldtype": "Link", "options": "Mietobjekt", "width": 150},
        {"label": _("Schäden"), "fieldname": "damages", "fieldtype": "Small Text", "width": 120},
        {"label": _("Lärmig"), "fieldname": "loud", "fieldtype": "Check", "width": 60},
        {"label": _("Reserviert"), "fieldname": "reserved", "fieldtype": "Check", "width": 80},
        {"label": _("Grösse[m2]"), "fieldname": "size", "fieldtype": "Data", "width": 80},
        {"label": _("Bemerkungen"), "fieldname": "notes", "fieldtype": "Small Text", "width": 250}
    ]

def get_data(filters):
    additional_filters = ''
    if filters.total_object:
        additional_filters += " AND `tabMietvertrag`.`total_object` = '" + filters.total_object + "'"
    if filters.object_name:
        additional_filters += " AND `tabMietobjekte`.`object_name` = '" + filters.object_name + "'"
    if not filters.disable_check:
        additional_filters += " AND `tabMietobjekt`.`reserved` = '" + str(filters.reserved) + "'"
        additional_filters += " AND `tabMietobjekt`.`loud` = '" + str(filters.loud) + "'"

    sql_query="""
        SELECT 
            `tabMietvertrag`.`name` AS `mietvertrag`,
            `tabMietvertrag`.`total_object` AS `total_object`,
            `tabMietobjekte`.`object_name` AS `object_name`,
            `tabMietobjekt`.`damages` AS `damages`,
            `tabMietobjekt`.`loud` AS `loud`,
            `tabMietobjekt`.`reserved` AS `reserved`,
            `tabMietobjekt`.`size` AS `size`,
            `tabMietobjekt`.`notes` AS `notes`,
            `tabMietvertrag`.`contract_start` AS `contract_start`,
            `tabMietvertrag`.`contract_end` AS `contract_end`
        FROM `tabMietvertrag`
        LEFT JOIN `tabMietobjekte` ON `tabMietvertrag`.`name` = `tabMietobjekte`.`parent`
        LEFT JOIN `tabMietobjekt` ON `tabMietvertrag`.`object_name` = `tabMietobjekt`.`name`
        WHERE `tabMietvertrag`.`docstatus` < 2
        AND `tabMietvertrag`.`contract_start` > '{date}'
        OR `tabMietvertrag`.`contract_end` < '{date}'{additional_filters}
        """.format(date=filters.date, additional_filters=additional_filters)
        
    data = frappe.db.sql(sql_query, as_dict=1)
    
    return data
