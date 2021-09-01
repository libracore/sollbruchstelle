from frappe import _

def get_data():
    return {
        'fieldname': 'mietvertrag',
        'transactions': [
            {
                'label': _("Kündigung"),
                'items': ['Kuendigung']
            },
            {
                'label': _("Nachtrag"),
                'items': ['Mietvertrag']
            },
            {
                'label': _("Abnahmeprotokoll"),
                'items': ['Abnahmeprotokoll']
            },
            {
                'label': _("Sales Invoice"),
                'items': ['Sales Invoice']
            }
        ]
    }
