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
        {"label": _("Gesamtobjekt"), "fieldname": "total_object", "fieldtype": "Link", "options": "Gesamtobjekt", "width": 90},
        {"label": _("Mietobjekt"), "fieldname": "object_name", "fieldtype": "Link", "options": "Mietobjekt", "width": 100},
        {"label": _("Schäden"), "fieldname": "damages", "fieldtype": "Small Text", "width": 120},
        {"label": _("Lärmig"), "fieldname": "loud", "fieldtype": "Check", "width": 60},
        {"label": _("Reserviert"), "fieldname": "reserved", "fieldtype": "Check", "width": 60},
        {"label": _("Grösse[m2]"), "fieldname": "size", "fieldtype": "Data", "width": 60},
        {"label": _("Mietbeginn"), "fieldname": "contract_start", "fieldtype": "Date", "width": 90},
        {"label": _("Mietende"), "fieldname": "contract_end", "fieldtype": "Date", "width": 90},
        {"label": _("Firma"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 100},
        {"label": _("Kunde 1"), "fieldname": "contact", "fieldtype": "Link", "options": "Contact", "width": 100},
        {"label": _("Kunde 2"), "fieldname": "contact_2", "fieldtype": "Link", "options": "Contact", "width": 100},
        {"label": _("Notizen Mietobj."), "fieldname": "notes", "fieldtype": "Small Text", "width": 250}
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
            `tabMietvertrag`.`contract_end` AS `contract_end`,
            `tabMietvertrag`.`customer` AS `customer`,
            `tabMietvertrag`.`contact` AS `contact`,
            `tabMietvertrag`.`contact_2` AS `contact_2`
        FROM `tabMietvertrag`
        LEFT JOIN `tabMietobjekte` ON `tabMietvertrag`.`name` = `tabMietobjekte`.`parent`
        LEFT JOIN `tabMietobjekt` ON `tabMietvertrag`.`object_name` = `tabMietobjekt`.`name`
        WHERE `tabMietvertrag`.`docstatus` < 2 {additional_filters}
        AND `tabMietvertrag`.`contract_start` <= '{date}'
        AND `tabMietvertrag`.`contract_end` >= '{date}'
        """.format(date=filters.date, additional_filters=additional_filters)
        
    data = frappe.db.sql(sql_query, as_dict=1)
    
    return data
