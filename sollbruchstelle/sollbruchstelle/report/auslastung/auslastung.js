// Copyright (c) 2021, Libracore AG and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Auslastung"] = {
    "filters": [
                    {
                        "fieldname":"date",
                        "label": __("Date"),
                        "fieldtype":"Date",
                        "default": frappe.datetime.get_today()
                    },
                    {
                        "fieldname":"total_object",
                        "label": __("Gesamtobjekt"),
                        "fieldtype":"Link",
                        "options": "Gesamtobjekt"
                    },
                    {
                        "fieldname":"object_name",
                        "label": __("Mietobjekt"),
                        "fieldtype":"Link",
                        "options": "Mietobjekt"
                    }
    ]
};
