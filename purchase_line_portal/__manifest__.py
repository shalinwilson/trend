{
    'name': 'Purchase Website Portal',
    'version': '17.0.1.1',
    'summary': 'Extending the purchase portal',
    'description': 'Purchase Portal',
    'category': 'Purchase/Purchase',
    'author': 'Odoo',
    'website': 'www.odoo.com',
    'depends': ['purchase', 'portal'],
    'data': [
        'views/template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'purchase_line_portal/static/src/js/main.js',
        ],
    },
    'installable': True,
    'auto_install': False
}
