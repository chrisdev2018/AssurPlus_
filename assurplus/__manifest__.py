# -*- coding: utf-8 -*-
{
    'name': "AssurPlus",

    'summary': """Gestion des assurances automobiles""",

    'description': """
        Ce module est conçu pour la gestion automatique de la
        procdure de traitement des opérations dans un bureau d'assurance.
        Permet de Collecter les informations d'un assuré ainsi que celles de son véhicule
        de les sauvegarder, ensuite de les restituer au besoin.
    """,

    'author': "Christian FOMEKONG",
    'website': "https://github.com/chrisdev2018",

    'category': 'Dev',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menus_views.xml',
        'views/assure.xml',
        'views/prime.xml'

    ],
    'installable': True,
    'application': True,
    
}