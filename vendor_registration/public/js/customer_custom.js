let nanoid=(t=21)=>{
    let e="",r=crypto.getRandomValues(new Uint8Array(t));for(;t--;){let n=63&r[t];e+=n<36?n.toString(36):n<62?(n-26).toString(36).toUpperCase():n<63?"_":"-"}
    return e;
}

frappe.ui.form.on("Customer", {
    refresh: function(frm) {
        if (!frm.is_new() && !frm.doc.customer_update_to) {
            frm.add_custom_button(__('Update Change'), function() {
    
                var new_cust = frappe.model.copy_doc(frm.doc);
                // update value to new_cust like from where it has been copied
                new_cust.customer_name = "UPDATE "+frm.doc.name+"_"+nanoid(10)
                new_cust.customer_update_to = frm.doc.name
                new_cust.disabled = 1
                let df = frappe.meta.get_docfield(new_cust.doctype, "disabled", new_cust.name);
                df.read_only = 1
                frappe.set_route('Form', 'Customer', new_cust.name);
            })
        }
    }
})