# -*- coding: utf-8 -*-
{
    'name': "Event Management",

    'summary': """
        Manage event with custom behavior""",

    'description': """
        Event Management
    """,
    'sequence': -110,
    'author': "Nomow",
    'website': "http://www.me.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing/Events',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'event'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/organizer_view.xml',
        'views/event_inherit_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3'
}
