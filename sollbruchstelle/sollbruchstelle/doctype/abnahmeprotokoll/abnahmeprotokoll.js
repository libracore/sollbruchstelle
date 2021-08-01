// Copyright (c) 2021, Libracore AG and contributors
// For license information, please see license.txt

frappe.ui.form.on('Abnahmeprotokoll', {
	onload: function(frm) {

		frm.page.add_menu_item(__("Custom BTN"), function() {
					console.log("Custom BTN Yeah!!!")
		 });
});
