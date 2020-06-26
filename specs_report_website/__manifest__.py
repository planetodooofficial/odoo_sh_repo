{
    'name': 'Product Specs Report',
    'category': 'Website',
    'sequence': 100,
    'summary': 'Get specification reports for products',
    'website': '',
    'version': '1.0',
    'description': "",
    'depends': ['website', 'sale', 'website_payment', 'website_sale', 'website_mail', 'website_form', 'website_rating', 'digest', 'product', 'base','stock','purchase_stock'],
    'data': [
        'views/template.xml',
        'views/specification_view.xml',
        'views/lot_serial_no_view.xml',
        'views/purchased_lot_portal_template.xml',
        'report/product_specification_report.xml',
        'report/product_specification_template.xml',
        'report/coa_report.xml',
        'report/coa_report_template.xml',

    ],
    'demo': [

    ],
    'qweb': [],
    'installable': True,
    'application': True,
}
