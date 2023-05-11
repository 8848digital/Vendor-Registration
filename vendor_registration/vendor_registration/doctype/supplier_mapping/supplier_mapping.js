// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Supplier Mapping', {
	validate: function(frm) {
		cur_frm.get_field('supplier_field_mapping').grid.grid_rows[0].row.show()
	}
});

frappe.ui.form.on('Supplier Field Mapping', {
	supplier_field_mapping_add: function(frm, cdt, cdn) {
		// first row has bug does not update option so hide the row.
		get_supplier_fields()
				.then((data) => {
					let supplier_registration_options = data.message[0]
					let supplier_options = data.message[1]
					cur_frm.get_field('supplier_field_mapping').grid.grid_rows[0].row.hide()
					frappe.meta.get_docfield("Supplier Field Mapping", "supplier_registration_field", cur_frm.doc.name).options = [""].concat(supplier_registration_options)
					frappe.meta.get_docfield("Supplier Field Mapping", "supplier_field", cur_frm.doc.name).options = [""].concat(supplier_options)
				})
	},
	supplier_registration_field: async function(frm, cdt, cdn) {
		let child = locals[cdt][cdn]
		await frappe.call({
			method: "vendor_registration.utils.get_fieldtype",
			args: {
				doctype: "Supplier Registration",
				fieldname: child.supplier_registration_field
			},
			callback: function(r) {
				frappe.model.set_value(cdt, cdn, "registration_datatype", r.message)
			}
		})
	},
	supplier_field: async function(frm, cdt, cdn) {
		let child = locals[cdt][cdn]
		await frappe.call({
			method: "vendor_registration.utils.get_fieldtype",
			args: {
				doctype: "Supplier",
				fieldname: child.supplier_field
			},
			callback: function(r) {
				frappe.model.set_value(cdt, cdn, "supplier_datatype", r.message)
			}
		})
	}
});

async function get_supplier_fields() {
	return await frappe.call({
		method: "vendor_registration.utils.get_doc_field",
		args: {
			doctype: "Supplier Registration",
			another_doctype: "Supplier",
		}
	})
}