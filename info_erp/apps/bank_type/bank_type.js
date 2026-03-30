// Copyright (c) 2024, Avangenio and contributors
// For license information, please see license.txt

frappe.ui.form.on("Bank Type", {
  validate(frm) {
    if (frm.doc.code) {
      if (frm.doc.code.length != 2) {
        frappe.msgprint(__("The code length must be 2 digits"));
        frappe.validated = false;
      } else if (!cuba.utils.is_number(frm.doc.code)) {
        frappe.msgprint(__("The code must be numeric"));
        frappe.validated = false;
      }
    }
  },
});
