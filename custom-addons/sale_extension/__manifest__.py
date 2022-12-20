{
    'name': 'Sale Extension',
    'sequence': 0,
    'version': '16.0',
    'summary': 'extension on the Sale level',
    'description': 'Sale Extension',
    'category': 'Productivity',
    'depends': ['sale', 'mail'],
    'data': [
        'views/sale_container_menu.xml',
        "views/sale_order_extension.xml",
        "views/sale_order_line_extension.xml"
    ],
    'installable': True,
    'application': False,
    'auto_install': False





}
