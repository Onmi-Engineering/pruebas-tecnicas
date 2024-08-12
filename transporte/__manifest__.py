{
    'name': 'TRANSPORTES',
    'version': '17.0.0.1',
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
        'security/ir_model_access.xml',
        'views/menuitem.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
