// Copyright (c) 2022, General Software Inc and contributors
// For license information, please see license.txt

function on_validate(frm) {
  let code = frm.doc.code;
  if (code) {
    let valid = /^\d*\.?\d*$/.test(code);
    if (!valid) {
      frappe.validated = false;
      frappe.msgprint(__("Code field must be numeric"));
    }
  }
}

function on_after_save(frm) {
  let name =
    frm.doc.code +
    "-" +
    frm.doc.department +
    "-" +
    frm.doc.designation +
    "-" +
    frm.doc.salary_group;
  if (name !== frm.doc.name) {
    frappe.route_flags.replace_route = true;
    frappe.router.set_route("Form", frm.doc.doctype, name);
  }
}

frappe.ui.form.on("Job Position", {
  validate: on_validate,
  after_save: on_after_save,
});
