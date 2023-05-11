# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.delete_doc import delete_from_table
class SupplierUpdateApproval(Document):
	

	def on_update(self):
		if self.workflow_state == "Approved":
			# update the existing supplier
			existing_supplier = frappe.get_doc("Supplier", self.supplier)
			updated_supplier = frappe.get_doc("Supplier", self.update_supplier)
			doc = frappe.copy_doc(updated_supplier)
			doc.supplier_name = existing_supplier.name # new supp has existing name
			# delete old supplier and save new with same name(link will not affected)
			delete_from_table("Supplier", existing_supplier.name, [], existing_supplier)
			# update value
			doc.disabled = 0
			doc.supplier_update_from = ""
			doc.save(ignore_permissions=True)
