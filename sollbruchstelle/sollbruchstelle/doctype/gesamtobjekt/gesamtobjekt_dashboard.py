from frappe import _

def get_data():
    return {
        'fieldname': 'total_object',
        'transactions': [
            {
                'label': _("Mietobjekt"),
                'items': ['Mietobjekt']
            }
        ]
    }
