# -*- encoding: utf-8 -*-

{
    'name': 'Filter Financial reports by Analytic Account',
    'summary': 'Filter Financial reports by Analytic Account',
    'author': 'Srikesh Infotech',
    'license': "OPL-1",
    'description': """
            This module allows you to  filter Financial Reports by analytic account.

    """,
    'website': 'http://www.srikeshinfotech.com',
    'depends': ['account','skit_account_reports'],  
    'images': ['images/main_screenshot.png'],
    'data': ['views/account_analytic_filter.xml',
            'views/general_ledger_account_analytic.xml',
             
    ],
    
    'installable': True,
    'application': True,
}