# Copyright (c) 2022, General Software Inc and Contributors
# See license.txt

from unittest.mock import Mock, patch

import frappe
from frappe.tests.utils import FrappeTestCase

from .job_position import JobPosition


class TestJobPosition(FrappeTestCase):
    def test_validate_req_code_field(self):

        job_position = frappe.get_doc(
            {
                "doctype": "Job Position",
                "designation": "Designation_Test",
                "salary_group": "Salary Group",
                "department": "Department Test",
            }
        )

        self.assertRaises(frappe.MandatoryError, job_position._validate_mandatory)

    def test_validate_req_department_field(self):

        job_position = frappe.get_doc(
            {
                "doctype": "Job Position",
                "designation": "Designation_Test",
                "code": "code Test",
                "salary_group": "Salary Group",
            }
        )

        self.assertRaises(frappe.MandatoryError, job_position._validate_mandatory)

    def test_validate_req_salary_group_field(self):

        job_position = frappe.get_doc(
            {
                "doctype": "Job Position",
                "designation": "Designation_Test",
                "code": "code Test",
                "department": "Department Test",
            }
        )

        self.assertRaises(frappe.MandatoryError, job_position._validate_mandatory)

    def test_validate_req_designation_field(self):

        job_position = frappe.get_doc(
            {
                "doctype": "Job Position",
                "code": "code Test",
                "salary_group": "Salary Group",
                "department": "Department Test",
            }
        )

        self.assertRaises(frappe.MandatoryError, job_position._validate_mandatory)

    def test_rename_job_position_on_update(self):
        """When change any field on a job position.
        it should rename the job position on db
        """

        job_position = Mock(
            doctype="Job Position",
            name="Old Name",
            code="Code Test",
            designation="Designation Test",
            salary_group="Salary Group Test",
            department="Department Test",
        )

        with patch(JobPosition.__module__ + ".frappe") as mock_frappe:

            def rename_doc(*args, **kwargs):
                frappe.flags.update_job_position_name = True

            mock_frappe.rename_doc.side_effect = rename_doc

            JobPosition.on_update(job_position)

        self.assertTrue(frappe.flags.update_job_position_name)
