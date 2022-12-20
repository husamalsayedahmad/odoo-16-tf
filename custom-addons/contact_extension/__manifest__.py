{
    'name': 'Contact Extension',
    'sequence': -100,
    'version': '16.0',
    'summary': 'extension on the contact Module',
    'description': 'Contact Extension',
    'category': 'Sales',
    'depends': ['contacts', 'stock'],
    'data': [
            'security/security.xml',
            'views/otherinfo_tab.xml',
            'views/sales_and_purchase.xml',
            'views/purchase_tab.xml',
            'views/main_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False





}
