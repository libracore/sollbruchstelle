from frappe import _

def get_data():
    return {
        'fieldname': 'nachtrag',
        'transactions': [
            {
                'label': _("Abnahmeprotokoll"),
                'items': ['Abnahmeprotokoll']
            }
        ]
    }
