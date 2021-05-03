# -*- coding: utf-8 -*-
{
    'name': "Web Widget Many2Many Tags Link",

    'summary': """
        Makes the many2many_tags widget clickable.
    """,

    'description': """
        If you click on the tag widget, you will be redirected to related model.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Cusotomization',
    'version': '13.0.1.0.0',

    'depends': ['base'],

    'data': [
        'views/assets.xml',
    ],

    'qweb': [
        "static/src/xml/fields_templates.xml",
    ],

    'installable': True,
    'application': False,
}