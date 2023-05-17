// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Update Approval', {
	refresh: function(frm) {
		$(
			frappe.render_template("version_view", { doc: frm.doc, data: JSON.parse(frm.doc.data) })
		).appendTo(frm.fields_dict.table_html.$wrapper.empty());
	}
});
