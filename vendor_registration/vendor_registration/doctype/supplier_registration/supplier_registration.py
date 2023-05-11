# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SupplierRegistration(Document):
	

	def on_update(self):
		if self.workflow_state == "Approved":
			# create supplier map the field value from Supplier Mapping
			map = frappe.get_doc("Supplier Mapping").supplier_field_mapping
			new_supplier = frappe.new_doc("Supplier")
			# self has supplier registration field
			for i in map:
				new_supplier.__dict__[i.supplier_field] = self.__dict__[i.supplier_registration_field]
			new_supplier.save()
