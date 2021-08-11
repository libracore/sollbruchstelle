// Copyright (c) 2021, Libracore AG and contributors
// For license information, please see license.txt

frappe.ui.form.on('Email Group', {
	refresh(frm) {
		frm.add_custom_button(__("Import from Total Object"), function() {
            total_object_prompt(frm);
        }, __("Action"));
	}
})

function total_object_prompt(frm) {
    frappe.prompt([
            {'fieldname': 'total_object', 'fieldtype': 'Link', 'options': 'Gesamtobjekt', 'label': 'Gesamtobjekt', 'reqd': 1}  
        ],
        function(values){
            fetch_subscribers(values.total_object);
        },
        'Gesamtobjekt',
        'Auswählen'
    )
}

function fetch_subscribers(total_object) {
    if (total_object) {
        frappe.call({
            method: 'sollbruchstelle.sollbruchstelle.newsletter.newsletter.get_subscribers',
            args: {
                'total_object': total_object,
                'email_group': cur_frm.doc.name
            },
            callback: function(r) {
                if(r.message) {
                    var subscribers = r.message;
                    cur_frm.reload_doc();
                    frappe.msgprint("Es wurde(n) " + subscribers.qty + " Adresse(n) hinzugefügt, " + subscribers.duplicate + " wurde(n) übersprungen da diese(r) bereits vorhanden war(en).");
                } else {
                    frappe.throw("Keine E-Mail Adressen gefunden.");
                }
            }
        });
    } else {
        frappe.throw("Bitte ein Gesamtobjekt auswählen!");
    }
}
