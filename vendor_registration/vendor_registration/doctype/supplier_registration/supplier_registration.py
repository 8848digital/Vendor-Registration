# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SupplierRegistration(Document):


	def on_update(self):
		if self.get_doc_before_save() and (self.workflow_state != self.get_doc_before_save().workflow_state and self.workflow_state == "Approved"):
			# create supplier map the field value from Supplier Mapping
			map = frappe.get_doc("Supplier Mapping").supplier_field_mapping
			new_supplier = frappe.new_doc("Supplier")
			# self has supplier registration field
			for i in map:
				new_supplier.__dict__[i.doc_field] = self.__dict__[i.registration_field]
			new_supplier.save()
			# update new supplier name to supplier registration
			frappe.db.sql(f'update `tabSupplier Registration` set supplier_created="{new_supplier.name}" where name="{self.name}"')
			frappe.db.commit()
			## create Address and link address
			addr = frappe.new_doc('Address')
			addr.address_title = self.get('address_title')
			addr.address_type = self.get('address_type')
			addr.address_line1 = self.get('address_line1')
			addr.address_line2 = self.get('address_line2')
			addr.city = self.get('city')
			addr.state = self.get('state')
			addr.country = self.get('country')
			addr.pincode = self.get('postal_code')
			addr.email_id = self.get('email_id')
			addr.phone = self.get('mobile_no')
			# link address
			addr.append('links',{
				'link_doctype': "Supplier",
				'link_name': new_supplier.name
			})
			addr.append('links',{
				'link_doctype': "Supplier Registration",
				'link_name': self.name
			})
			addr.save()
