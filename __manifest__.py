{
    'name': 'Gestión de Vehiculos',
    'version': '1.0',
    'summary': 'Gestión de vehículos de la empresa.',
    'description': 'Este módulo gestiona los vehiculos disponibles de la empresa. ',
    'author': 'Diego Rodríguez',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv', #Control de acceso
        'views/vehiculo_views.xml', #Vista del módulo
    ],
    'installable': True,
    'application': True,
}