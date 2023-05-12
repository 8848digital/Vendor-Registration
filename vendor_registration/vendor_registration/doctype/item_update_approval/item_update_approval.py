# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.delete_doc import delete_from_table

class ItemUpdateApproval(Document):
	
	def on_update(self):
		if self.workflow_state == "Approved":
			# update the existing item
			existing_item = frappe.get_doc("Item", self.item)
			updated_item = frappe.get_doc("Item", self.update_item)
			doc = frappe.copy_doc(updated_item)
			doc.item_code = existing_item.item_code # new item has existing name
			# delete old item and save new with same name(link will not affected)
			delete_from_table("Item", existing_item.name, [], existing_item)
			# update value
			doc.disabled = 0
			doc.item_update_to = ""
			doc.save(ignore_permissions=True)
