{
    'name': 'Misa API',
    'version': '1.0.0',
    'sequence': -50,
    'author': 'WATATEK',
    'website': 'www.watatek.com',
    'category': 'API',
    'summary': 'MISA API',
    'description': 'MISA API',
    'depends': ['base'],
    'data': [
        'data/misa_api_action.xml',
        'view/misa_api_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/misa_api/static/src/scss/grid_data.scss',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}