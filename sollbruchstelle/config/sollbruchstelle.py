from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": _("Kundendokumente"),
            "items": [
                   {
                       "type": "doctype",
                       "name": "Customer",
                       "label": _("Kunde/Firma"),
                       "description": _("Customer")
                   },
                   {
                       "type": "doctype",
                       "name": "Contact",
                       "label": _("Kontakt/-person"),
                       "description": _("Contact")
                   },
                   {
                       "type": "doctype",
                       "name": "Sales Invoice",
                       "label": _("Kundenrechnung"),
                       "description": _("Sales Invoice")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Entry",
                       "label": _("Kundenzahlung"),
                       "description": _("Payment Entry")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Reminder",
                       "label": _("Zahlungserinnerung"),
                       "description": _("Payment Reminder")
                   }
            ]
        },
        {
            "label": _("Tagesgeschäft"),
            "items": [
                   {
                       "type": "doctype",
                       "name": "Gesamtobjekt",
                       "label": _("Gesamtobjekt"),
                       "description": _("Gesamtobjekt")
                   },
                   {
                       "type": "doctype",
                       "name": "Mietobjekt",
                       "label": _("Mietobjekt/Raum"),
                       "description": _("Mietobjekt")
                   },
                   {
                       "type": "doctype",
                       "name": "Mietvertrag",
                       "label": _("Mietvertrag"),
                       "description": _("Mietvertrag")
                   },
                   {
                       "type": "doctype",
                       "name": "Nachtrag",
                       "label": _("Nachtrag"),
                       "description": _("Nachtrag")
                   },
                   {
                       "type": "doctype",
                       "name": "Kuendigung",
                       "label": _("Kündigung"),
                       "description": _("Kuendigung")
                   },
                   {
                       "type": "doctype",
                       "name": "Abnahmeprotokoll",
                       "label": _("Abnahmeprotokoll"),
                       "description": _("Abnahmeprotokoll")
                   },
                   {
                       "type": "doctype",
                       "name": "Contact",
                       "label": _("Schluesselquittung"),
                       "description": _("Schluesselquittung")
                   }                            
            ]
        },
        {
            "label": _("Auswertungen"),
            "items": [
                   {
                       "type": "report",
                       "name": "leerstandsliste",
                       "label": _("Leerstandsliste"),
                       "doctype": "Leerstandsliste",
                       "is_query_report": True
                   },
                   {
                       "type": "report",
                       "name": "Mieterspiegel",
                       "label": _("Mieterspiegel"),
                       "doctype": "Mietvertrag",
                       "is_query_report": True
                   }                                  
            ]
        },
        {
            "label": _("Formularansicht des Portals"),
            "items": [
                   {
                       "type": "doctype",
                       "name": "Aushang",
                       "label": _("Aushang"),
                       "description": _("Aushang")
                   },
                   {
                       "type": "doctype",
                       "name": "Externer Auftrag",
                       "label": _("Externer Auftrag"),
                       "description": _("Externer Auftrag")
                   },
                   {
                       "type": "doctype",
                       "name": "Raumbeschriftung",
                       "label": _("Raumbeschriftung"),
                       "description": _("Raumbeschriftung")
                   }                              
            ]
        },
        {
            "label": _("Externe/Einkauf"),
            "items": [
                   {
                       "type": "doctype",
                       "name": "Supplier",
                       "label": _("Lieferant"),
                       "description": _("Supplier")
                   },
                   {
                       "type": "doctype",
                       "name": "Purchase Order",
                       "label": _("Lieferantenbestellung"),
                       "description": _("Purchase Order")
                   },
                   {
                       "type": "doctype",
                       "name": "Purchase Receipt",
                       "label": _("Bestellbestätigung Lieferant"),
                       "description": _("Purchase Receipt")
                   },
                   {
                       "type": "doctype",
                       "name": "Purchase Invoice",
                       "label": _("Wareneingang"),
                       "description": _("Purchase Invoice")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Entry",
                       "label": _("Lieferantenzahlung"),
                       "description": _("Payment Entry")
                   }
            ]
        },
        {
            "label": _("HR"),
            "items": [
                   {
                       "type": "doctype",
                       "name": "Employee",
                       "label": _("Employee"),
                       "description": _("Employee")
                   },
                   {
                       "type": "doctype",
                       "name": "Leave Application",
                       "label": _("Leave Application"),
                       "description": _("Leave Application")
                   },                   
                   {
                       "type": "doctype",
                       "name": "Leave Allocation",
                       "label": _("Leave Allocation"),
                       "description": _("Leave Allocation")
                   },
                   {
                       "type": "doctype",
                       "name": "Worktime Settings",
                       "label": _("Worktime Settings"),
                       "description": _("Worktime Settings")
                   },
                   {
                       "type": "report",
                       "doctype": "Timesheet",
                       "name": "Worktime Overview",
                       "label": _("Worktime Overview"),
                       "description": _("Worktime Overview"),
                       "is_query_report": True
                   }
            ]
        },
        {
            "label": _("Accounting"),
            "items": [
                   {
                       "type": "page",
                       "name": "bank_wizard",
                       "label": _("Bank Wizard"),
                       "description": _("Bank Wizard")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Proposal",
                       "label": _("Payment Proposal"),
                       "description": _("Payment Proposal")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Reminder",
                       "label": _("Payment Reminder"),
                       "description": _("Payment Reminder")
                   },
                   {
                       "type": "report",
                       "name": "General Ledger",
                       "doctype": "GL Entry",
                       "is_query_report": True,
                   },
                   {
                       "type": "doctype",
                       "name": "Bankkonto",
                       "label": _("Bankkonto"),
                       "description": _("Bankkonto")
                   }
            ]
        },
        {
            "label": _("Stammdaten"),
            "items": [
                   {
                       "type": "doctype",
                       "name": "Terms",
                       "label": _("Textvorlagen"),
                       "description": _("Textvorlagen")
                   },
                   {
                       "type": "doctype",
                       "name": "Schliessanlage",
                       "label": _("Schliessanlage"),
                       "description": _("Schliessanlage")
                   },
                   {
                       "type": "doctype",
                       "name": "SchluesselBatchNr",
                       "label": _("Schlüsselnr/Batchnr"),
                       "description": _("Schlüsselnr/Batchnr")
                   },                  
                   {
                       "type": "doctype",
                       "name": "Stockwerk",
                       "label": _("Stockwerk"),
                       "description": _("Stockwerk")
                   },
                   {
                       "type": "doctype",
                       "name": "Priorisierung",
                       "label": _("Priorisierung"),
                       "description": _("Priorisierung")
                   },
                   {
                       "type": "doctype",
                       "name": "Nutzungsart",
                       "label": _("Nutzungsart"),
                       "description": _("Nutzungsart")
                   },
                   {
                       "type": "doctype",
                       "name": "Bodenbelag",
                       "label": _("Bodenbelag"),
                       "description": _("Bodenbelag")
                   },
                   {
                       "type": "doctype",
                       "name": "Projektname",
                       "label": _("Projektname"),
                       "description": _("Projektname")
                   }
            ]
        }
    ]
