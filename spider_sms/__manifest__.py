# -*- coding: utf-8 -*-
{
    'name': "spider sms",

    'summary': """
        Send SMS to your partners""",

    'description': """
        Use SMS local providers to send SMS to your partners
    """,

    'author': "Parfait BENE",
    'website': "http://www.parfaitbene.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/spider_sms.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
