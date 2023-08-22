# -*- coding: utf-8 -*-
{
    'name': "ESIS_Logistique",

    'summary': """
        Application pour la gestion de la logistique à ESIS""",

    'description': """
    Avec ce module(application) on peut enregistrer des materiels dans le stock et suivre la consommations genre la quantité en temps réél
    partant des enregistrements des entrées et des sorties, on peut aussi enregistré toutes les allocations des materiels pour garder la tracabilité
    des évenements à la logistique, lors de l'allocation la quantité des materiels en stock est controlée, on ne peut faire une allocation avec 
    un stock vide, on ne peut faire une allocation des plus des materièles que la quantité des materiles en stock.
    On peut aussi constitué un rapport et pouvoir l'envoyer par mail, on peut envoyer un rapport ciblé d'un certain jour ou une certaine personne,
    on peut aussi faire un filtrage et envoyé seulement un rapport des éléments enregistrés dans un mois,... 
    """,

    'author': "BlackDevs",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/main.xml',
        'views/gerer_materiel.xml',
        'views/gerer_demande.xml',
        'views/gerer_rapport.xml',
        'views/categorie.xml',
        'views/mes_tables.xml',
        'views/effect_dmd.xml',
        'views/alloc_mat.xml',
        'views/allocation_main.xml',
        'data/mail_template.xml',

        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
