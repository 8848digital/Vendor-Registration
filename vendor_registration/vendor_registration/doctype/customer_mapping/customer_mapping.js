// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Mapping', {
	refresh: function(frm) {
		get_customer_fields()
			.then((data) => {
				let customer_registration_options = data.message[0]
				let customer_options = data.message[1]
				frappe.meta.get_docfield("Field Mapping", "registration_field", cur_frm.doc.name).options = [""].concat(customer_registration_options)
				frappe.meta.get_docfield("Field Mapping", "doc_field", cur_frm.doc.name).options = [""].concat(customer_options)
			})
	},
	validate: function(frm) {
		cur_frm.get_field('customer_field_mapping').grid.grid_rows[0].row.show()
	}
});

frappe.ui.form.on('Field Mapping', {
	customer_field_mapping_add: function(frm, cdt, cdn) {
		// first row has bug does not update option so hide the row.
		// get_customer_fields()
		// 		.then((data) => {
		// 			let customer_registration_options = data.message[0]
		// 			let customer_options = data.message[1]
		// 			cur_frm.get_field('customer_field_mapping').grid.grid_rows[0].row.hide()
		// 			frappe.meta.get_docfield("Field Mapping", "registration_field", cur_frm.doc.name).options = [""].concat(customer_registration_options)
		// 			frappe.meta.get_docfield("Field Mapping", "doc_field", cur_frm.doc.name).options = [""].concat(customer_options)
		// 		})
	},
	registration_field: async function(frm, cdt, cdn) {
		let child = locals[cdt][cdn]
		await frappe.call({
			method: "vendor_registration.utils.get_fieldtype",
			args: {
				doctype: "Customer Registration",
				fieldname: child.registration_field
			},
			callback: function(r) {
				frappe.model.set_value(cdt, cdn, "registration_datatype", r.message)
			}
		})
	},
	doc_field: async function(frm, cdt, cdn) {
		let child = locals[cdt][cdn]
		await frappe.call({
			method: "vendor_registration.utils.get_fieldtype",
			args: {
				doctype: "Customer",
				fieldname: child.doc_field
			},
			callback: function(r) {
				frappe.model.set_value(cdt, cdn, "doc_datatype", r.message)
			}
		})
	}
});

async function get_customer_fields() {
	return await frappe.call({
		method: "vendor_registration.utils.get_doc_field",
		args: {
			doctype: "Customer Registration",
			another_doctype: "Customer",
		}
	})
}