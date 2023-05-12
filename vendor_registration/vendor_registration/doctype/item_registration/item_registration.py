# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemRegistration(Document):
	

	def on_update(self):
		if self.workflow_state == "Approved":
			# create customer map the field value from Customer Mapping
			map = frappe.get_doc("Item Mapping").item_field_mapping
			new_customer = frappe.new_doc("Item")
			# self has customer registration field
			for i in map:
				new_customer.__dict__[i.doc_field] = self.__dict__[i.registration_field]
			new_customer.save()
