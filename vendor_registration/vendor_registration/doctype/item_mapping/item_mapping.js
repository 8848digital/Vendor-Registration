// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Mapping', {
	refresh: function(frm) {
		get_item_fields()
			.then((data) => {
				let item_registration_options = data.message[0]
				let item_options = data.message[1]
				frappe.meta.get_docfield("Field Mapping", "registration_field", cur_frm.doc.name).options = [""].concat(item_registration_options)
				frappe.meta.get_docfield("Field Mapping", "doc_field", cur_frm.doc.name).options = [""].concat(item_options)
			})
	},
	validate: function(frm) {
		cur_frm.get_field('item_field_mapping').grid.grid_rows[0].row.show()
	}
});

frappe.ui.form.on('Field Mapping', {
	item_field_mapping_add: function(frm, cdt, cdn) {
		
	},
	registration_field: async function(frm, cdt, cdn) {
		let child = locals[cdt][cdn]
		await frappe.call({
			method: "vendor_registration.utils.get_fieldtype",
			args: {
				doctype: "Item Registration",
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
				doctype: "Item",
				fieldname: child.doc_field
			},
			callback: function(r) {
				frappe.model.set_value(cdt, cdn, "doc_datatype", r.message)
			}
		})
	}
});

async function get_item_fields() {
	return await frappe.call({
		method: "vendor_registration.utils.get_doc_field",
		args: {
			doctype: "Item Registration",
			another_doctype: "Item",
		}
	})
}