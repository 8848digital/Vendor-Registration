# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.delete_doc import delete_from_table
from frappe.desk.form.linked_with import get_child_tables_of_doctypes

class ItemUpdateApproval(Document):
	
	def on_update(self):
		if self.workflow_state == "Approved":
			# update the existing item
			existing_item = frappe.get_doc("Item", self.item)
			updated_item = frappe.get_doc("Item", self.update_item)
			
			doctype_fields = frappe.get_meta("Item").get_fieldnames_with_value()
			excluded_field = ['item_code', 'item_update_to', 'disabled', 'naming_series']
			fields = [field for field in doctype_fields if field not in excluded_field]
	
			child = get_child_tables_of_doctypes(['Item'])['Item']
			
			for i in fields:
				value= frappe.db.get_value("Item", updated_item.name, i)
				frappe.db.set_value(existing_item.doctype, existing_item.name, i, value)
			#child table doctype	
			for j in child:
				del_query = f'DELETE FROM `tab{j["child_table"]}` WHERE parent="{existing_item.name}"'
				# remove all the child table data from the existing Item table
				frappe.db.sql(del_query)
				for row in updated_item.get(j['fieldname']):
					
					row_name = row.name
					child_doc = frappe.get_doc(j['child_table'], row_name)
					child_doc.parent = existing_item.name
					child_doc.save(ignore_permissions=True)
			#before delete need to work on attachments
			# delete updated Item doctype
			delete_from_table("Item", updated_item.name, [], updated_item)
			frappe.db.commit()
