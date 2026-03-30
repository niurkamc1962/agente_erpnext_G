# Copyright (c) 2022, General Software Inc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import set_name_from_naming_options


class JobPosition(Document):
    def on_update(self):
        name = self.name
        autoname = frappe.get_meta(self.doctype).autoname
        set_name_from_naming_options(autoname, self)
        if self.name != name:
            frappe.rename_doc(self.doctype, name, self.name, force=True)
