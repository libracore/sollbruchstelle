from frappe import _

def get_data():
    return {
        'fieldname': 'object_name',
        'transactions': [
            {
                'label': _("Mietvertrag"),
                'items': ['Mietvertrag']
            },
            {
                'label': _("Raum"),
                'items': ['Raum']
            },
            {
                'label': _("Schluessel"),
                'items': ['Schluessel']
            }
        ]
    }
