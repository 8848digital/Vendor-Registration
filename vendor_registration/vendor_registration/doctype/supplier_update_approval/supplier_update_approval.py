# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.delete_doc import delete_from_table
from frappe.desk.form.linked_with import get_child_tables_of_doctypes

class SupplierUpdateApproval(Document):
	

	def on_update(self):
		if self.workflow_state == "Approved":
			# update the existing supplier
			existing_supplier = frappe.get_doc("Supplier", self.supplier)
			updated_supplier = frappe.get_doc("Supplier", self.update_supplier)
			
			doctype_fields = frappe.get_meta("Supplier").get_fieldnames_with_value()
			excluded_field = ['supplier_name', 'supplier_update_from', 'disabled', 'naming_series']
			fields = [field for field in doctype_fields if field not in excluded_field]
	
			child = get_child_tables_of_doctypes(['Supplier'])['Supplier']
			
			for i in fields:
				value= frappe.db.get_value("Supplier",updated_supplier.name,i)
				frappe.db.set_value(existing_supplier.doctype, existing_supplier.name, i, value)
			#child table doctype	
			for j in child:
				del_query = f'DELETE FROM `tab{j["child_table"]}` WHERE parent="{existing_supplier.name}"'
				frappe.db.sql(del_query)
				for row in updated_supplier.get(j['fieldname']):
					# existing_supplier.get(j['fieldname']) = []
					# remove all the child table data from the existing supplier table
					
					# frappe.db.set_value(existing_supplier.doctype, existing_supplier.name, row, value)
					row_name = row.name
					child_doc = frappe.get_doc(j['child_table'], row_name)
					child_doc.parent = existing_supplier.name
					child_doc.save(ignore_permissions=True)
			#before delete need to work on attachments
			# delete updated supplier doctype
			delete_from_table("Supplier", updated_supplier.name, [], updated_supplier)
			frappe.db.commit()