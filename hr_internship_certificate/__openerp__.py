# -*- coding: utf-8 -*-
##############################################################################
#
#   www.vertel.se
#
##############################################################################

{
    'name': 'Internship Certificate',
    'version': '0.1',
    'category': 'Human Resources',
    'description': """
Internship certificates
=======================

Report that is an internship certificate

    """,
    'author': 'Vertel AB',
    'license': 'AGPL-3',
    'website': 'http://www.vertel.se',
    'depends': ['hr_contract',],
    'data': [
        'hr_internship_certificate_data.xml',
        'hr_internship_certificate_view.xml',
        'hr_internship_certificate_report.xml',
       ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
