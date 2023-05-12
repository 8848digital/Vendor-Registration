import frappe


@frappe.whitelist()
def get_doc_field(doctype, another_doctype):
    
    doctype_fields = frappe.get_meta(doctype).get_fieldnames_with_value()
    fields = [field for field in doctype_fields if field != 'workflow_state']

    another_doctype_fields = frappe.get_meta(another_doctype).get_fieldnames_with_value()
    another_fields = [field for field in another_doctype_fields if field != 'workflow_state']
    return fields, another_fields

@frappe.whitelist()
def get_fieldtype(doctype, fieldname):
    if frappe.get_meta(doctype).get_field(fieldname):
        fieldtype = frappe.get_meta(doctype).get_field(fieldname).__dict__['fieldtype']
        return fieldtype
    return ""

def link_update_supplier(doc, method):
    if doc.supplier_update_from:
        # create new doc who has workflow
        new_doc = frappe.new_doc("Supplier Update Approval")
        new_doc.supplier = doc.supplier_update_from
        new_doc.update_supplier = doc.name
        new_doc.save(ignore_permissions=True)
        # pass
def link_update_customer(doc, method):
    if doc.customer_update_to:
        # create new doc who has workflow
        new_doc = frappe.new_doc("Customer Update Approval")
        new_doc.customer = doc.customer_update_to
        new_doc.update_customer = doc.name
        new_doc.save(ignore_permissions=True)

def link_update_item(doc, method):
    if doc.item_update_to:
        # create new doc who has workflow
        new_doc = frappe.new_doc("Item Update Approval")
        new_doc.item = doc.item_update_to
        new_doc.update_item = doc.name
        new_doc.save(ignore_permissions=True)
