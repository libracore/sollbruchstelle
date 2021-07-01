from frappe import _

def get_data():
    return {
        'fieldname': 'object_name',
        'transactions': [
            {
                'label': _("Mietvertrag"),
                'items': ['Mietvertrag']
            }
        ]
    }
