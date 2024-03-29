# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2011-2012 Serpent Consulting Services (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Fees Management",
    "version" : "1.2",
    "author" : "Serpent Consulting Services",
    "website" : "http://www.serpentcs.com",
    "category": "School Management",
    "complexity": "easy",
    "description": """A module to School Fees Management System.
     A Module support the following functionalities:
        1. Student Fees Management.
        2. Student Fees Receipt.
        3. Student Fees structure.
        4. Student Fees Register.
                    """,
    "depends" : [
        "base",
        "school",
        "account_voucher"
    ],
    "demo" : [
              "demo/school_fees_demo.xml"
              ],
    "data" : [
        "security/ir.model.access.csv",
        "school_fees_view.xml",
        "school_fees_sequence.xml",
        "student_fees_register_workflow.xml",
        "student_payslip_workflow.xml",
        "student_fees_register_report_view.xml",
        "student_payslip_report_view.xml",
    ],
  
    'test': [
        'test/school_fees_test.yml',
        'test/report_student_payslip_test.yml',
        'test/report_student_fees_register_test.yml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
