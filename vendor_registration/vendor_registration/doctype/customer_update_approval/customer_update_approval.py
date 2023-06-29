# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.delete_doc import delete_from_table
from frappe.desk.form.linked_with import get_child_tables_of_doctypes

class CustomerUpdateApproval(Document):
	

	def on_update(self):
		if self.workflow_state == "Approved":
			# update the existing customer
			existing_customer = frappe.get_doc("Customer", self.customer)
			updated_customer = frappe.get_doc("Customer", self.update_customer)
			
			doctype_fields = frappe.get_meta("Customer").get_fieldnames_with_value()
			excluded_field = ['customer_name', 'customer_update_to', 'disabled', 'naming_series']
			fields = [field for field in doctype_fields if field not in excluded_field]
	
			child = get_child_tables_of_doctypes(['Customer'])['Customer']
			
			for i in fields:
				value= frappe.db.get_value("Customer", updated_customer.name, i)
				frappe.db.set_value(existing_customer.doctype, existing_customer.name, i, value)
			#child table doctype	
			for j in child:
				del_query = f'DELETE FROM `tab{j["child_table"]}` WHERE parent="{existing_customer.name}"'
				# remove all the child table data from the existing Customer table
				frappe.db.sql(del_query)
				for row in updated_customer.get(j['fieldname']):
					
					row_name = row.name
					child_doc = frappe.get_doc(j['child_table'], row_name)
					child_doc.parent = existing_customer.name
					child_doc.save(ignore_permissions=True)
			#before delete need to work on attachments
			# delete updated Customer doctype
			delete_from_table("Customer", updated_customer.name, [], updated_customer)
			frappe.db.commit()
