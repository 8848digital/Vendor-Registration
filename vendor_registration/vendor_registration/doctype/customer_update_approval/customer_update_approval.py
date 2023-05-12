# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.delete_doc import delete_from_table

class CustomerUpdateApproval(Document):
	

	def on_update(self):
		if self.workflow_state == "Approved":
			# update the existing customer
			existing_customer = frappe.get_doc("Customer", self.customer)
			updated_customer = frappe.get_doc("Customer", self.update_customer)
			doc = frappe.copy_doc(updated_customer)
			doc.customer_name = existing_customer.name # new cust has existing name
			# delete old customer and save new with same name(link will not affected)
			delete_from_table("Customer", existing_customer.name, [], existing_customer)
			# update value
			doc.disabled = 0
			doc.customer_update_to = ""
			doc.save(ignore_permissions=True)
