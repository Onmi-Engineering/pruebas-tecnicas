{
    'name': 'TRANSPORTES',
    'version': '18.0.0.1',
    'summary': 'Prueba técnica OEng - Transportes',
    'description': 'Módulo de gestión de transportes (prueba técnica)',
    'category': 'Prueba nivel',
    'author': 'ONMI Engineering',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'delivery',
        'mrp',
    ],
    'data': [
        # Security
        'security/ir_model_access.xml',

        # Views
        'views/res_partner_views.xml',
        'views/transporte_solicitud_views.xml',

        # Menus
        'views/menuitem.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
