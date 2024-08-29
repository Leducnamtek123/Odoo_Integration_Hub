# -*- coding: utf-8 -*-
{
    'name': "tms",

    'summary': "About system management transpotation",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tms',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'fleet'],

    # always loaded
   'data': [
        # Security and Access Control
        #'security/security.xml',
        
        # Views
        # 'views/driver_views.xml',
        'views/tms_menus.xml',
        'views/driver_cash_advance_views.xml',
        'views/freight_invoicing_views.xml',
        'views/fuel_voucher_views.xml',
        'views/kits_views.xml',
        'views/places_views.xml',
        'views/kit_views.xml',
        'views/places_views.xml',
        'views/routes_views.xml',
        'views/travel_events_views.xml',
        'views/travel_expenses_views.xml',
        'views/truck_odometer_views.xml',
        'views/truck_red_tapes_views.xml',

        # Reports
        'reports/reports.xml',
        
        # Automated Actions
        'data/automated_actions.xml',
        
        # Data files (if any, like sample data)
        # 'data/sample_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'sequence': -50,
}

