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
        {"label": _("Mietvertrag"), "fieldname": "mietvertrag", "fieldtype": "Link", 'options': 'Mietvertrag', "width": 100},
        {"label": _("Gesamtobjekt"), "fieldname": "total_object", "fieldtype": "Link", "options": "Gesamtobjekt", "width": 102},
        {"label": _("Mietobjekt"), "fieldname": "object_name", "fieldtype": "Link", "options": "Mietobjekt", "width": 120},
        {"label": _("Mietbeginn"), "fieldname": "contract_start", "fieldtype": "Date", "width": 70},
        {"label": _("Mietende"), "fieldname": "contract_end", "fieldtype": "Date", "width": 70},
        {"label": _("Nutzungsart"), "fieldname": "usage_type", "fieldtype": "Link", "options": "Nutzungsart", "width": 100},
        {"label": _("Firma"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 100},
        {"label": _("Kunde 1"), "fieldname": "contact", "fieldtype": "Link", "options": "Contact", "width": 100},
        {"label": _("Kunde 2"), "fieldname": "contact_2", "fieldtype": "Link", "options": "Contact", "width": 100},
        {"label": _("Depothöhe"), "fieldname": "depot_amount", "fieldtype": "Currency", "width": 100}
    ]

def get_data(filters):
    additional_filters = ''
    if filters.total_object:
        additional_filters += " AND `tabMietvertrag`.`total_object` = '" + filters.total_object + "'"
    if filters.object_name:
        additional_filters += " AND `tabMietobjekte`.`object_name` = '" + filters.object_name + "'"

    sql_query="""
        SELECT 
            `tabMietvertrag`.`name` AS `mietvertrag`,
            `tabMietvertrag`.`total_object` AS `total_object`,
            `tabMietobjekte`.`object_name` AS `object_name`,
            `tabMietvertrag`.`contract_start` AS `contract_start`,
            `tabMietvertrag`.`contract_end` AS `contract_end`,
            `tabMietvertrag`.`usage_type` AS `usage_type`,
            `tabMietvertrag`.`customer` AS `customer`,
            `tabMietvertrag`.`contact` AS `contact`,
            `tabMietvertrag`.`contact_2` AS `contact_2`,
            `tabMietvertrag`.`depot_amount` AS `depot_amount`
        FROM `tabMietvertrag`
        LEFT JOIN `tabMietobjekte` ON `tabMietvertrag`.`name` = `tabMietobjekte`.`parent`
        WHERE `tabMietvertrag`.`docstatus` < 2
        AND `tabMietvertrag`.`contract_start` <= '{date}'
        AND `tabMietvertrag`.`contract_end` >= '{date}'{additional_filters}
        """.format(date=filters.date, additional_filters=additional_filters)
        
    data = frappe.db.sql(sql_query, as_dict=1)
    
    return data
