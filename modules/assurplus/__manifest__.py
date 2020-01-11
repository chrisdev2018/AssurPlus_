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

    'category': 'AssurPlus',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # Sécurité 
        'security/groups.xml',   
        'security/ir.model.access.csv',
        
        #Les vues
        'views/menus_views.xml',
        'views/assure_views.xml',
        'views/vehicule_views.xml',
        'views/prime_views.xml',
        'views/contrat_views.xml',
        'views/genre_views.xml',
        
        #Les rapport
        'reports/call_rapport_conditions_parti.xml',
        'reports/rapport_conditions_parti.xml',
    
    ],
    'installable': True,
    'application': True,
    
}