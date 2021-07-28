from frappe import _

def get_data():
    return {
        'fieldname': 'mietvertrag',
        'transactions': [
            {
                'label': _("Kündigung"),
                'items': ['Kuendigung']
            }
        ]
    }
