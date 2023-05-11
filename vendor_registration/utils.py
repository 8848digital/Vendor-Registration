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
    fieldtype = frappe.get_meta(doctype).get_field(fieldname).__dict__['fieldtype']
    return fieldtype

def link_update_supplier(doc, method):
    if doc.supplier_update_from:
        # create new doc who has workflow
        new_doc = frappe.new_doc("Supplier Update Approval")
        new_doc.supplier = doc.supplier_update_from
        new_doc.update_supplier = doc.name
        new_doc.save(ignore_permissions=True)
        # pass