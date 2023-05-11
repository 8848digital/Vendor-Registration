let nanoid=(t=21)=>{
    let e="",r=crypto.getRandomValues(new Uint8Array(t));for(;t--;){let n=63&r[t];e+=n<36?n.toString(36):n<62?(n-26).toString(36).toUpperCase():n<63?"_":"-"}
    return e;
}

frappe.ui.form.on("Supplier", {
    refresh: function(frm) {
        if (!frm.is_new() && !frm.doc.supplier_update_from) {
            frm.add_custom_button(__('Update Change'), function() {
    
                var new_sup = frappe.model.copy_doc(frm.doc);
                // update value to new_supp like from where it has been copied
                new_sup.supplier_name = "UPDATE "+frm.doc.name+"_"+nanoid(10)
                new_sup.supplier_update_from = frm.doc.name
                new_sup.disabled = 1
                let df = frappe.meta.get_docfield(new_sup.doctype, "disabled", new_sup.name);
                df.read_only = 1
                frappe.set_route('Form', 'Supplier', new_sup.name);
            })
        }
    }
})