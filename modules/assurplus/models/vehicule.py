# -*- coding: utf-8 -*-
from odoo import api, fields, models


list_cat = [('O1', 'O1'), ('O2_A', 'O2/A'), ('O2_B', 'O2/B'), ('O2_C', 'O2/C'), ('O3_A', 'O3/A'),
            ('O3_B', 'O3/B'), ('O4_A', 'O4/A'), ('O4/_', 'O4/B'), ('O4_C', 'O4/C'),
            ('O5/A', 'O5/A'), ('O5/B', 'O5/B'), ('O6', 'O6'), ('O7', 'O7'), ('O8', 'O8'),
            ('O9', 'O9'), ('1O', '1O')
            ]


class Vehicule(models.Model):
    _name = "assurplus.vehicule"

    name = fields.Char(
        string="Immatriculation",
        required=True
    )
    
    categorie = fields.Selection(
        string='', 
        selection=list_cat
    )
    

    # TODO: mettre une contrainte sql pour le name

    genre = fields.Selection(
        string="Genre",
        selection=[
            ('tri', 'Tricycle'),
            ('voi', 'Voiture'),
            ('cam', 'Camion'),
            ('mot', 'Moto')
        ]
    )

    marque = fields.Char(
        string="Marque"
    )

    chassis = fields.Char(
        string="N° Chassis",
        required=True
    )

    # TODO: mettre une contrainte sql pour le name

    zone = fields.Char(
        string="Zone de circulation"
    )

    usage = fields.Char(
        string="Usage"
    )

    puissance = fields.Integer(
        string="Puissance (en CV)"
    )

    source = fields.Selection(
        string="Source d'energie",
        selection=[
            ('ess', 'Essence'),
            ('gas', 'Gasoil'),
            ('elec', 'Electrique')
        ]
    )

    nb_place = fields.Integer(
        string="Nombre de places"
    )

    conducteur = fields.Many2one(
        string="Conducteur habituel",
        comodel_name="assurplus.assure"
    )
