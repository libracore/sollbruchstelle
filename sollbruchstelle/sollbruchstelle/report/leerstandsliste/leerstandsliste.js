// Copyright (c) 2021, Libracore AG and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Leerstandsliste"] = {
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
                    },
                    {
                        "fieldname":"reserved",
                        "label": __("Reserviert"),
                        "fieldtype":"Check"
                    },
                    {
                        "fieldname":"loud",
                        "label": __("Lärmig"),
                        "fieldtype":"Check"
                    },
                    {
                        "fieldname":"disable_check",
                        "label": __("alle Ergebnisse (deaktivier Checkboxen)"),
                        "fieldtype":"Check",
                        "default": 1
                    }
    ]
};
