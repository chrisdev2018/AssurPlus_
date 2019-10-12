# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Vehicule(models.Model):
    _name = "assurplus.vehicule"

    name = fields.Char(
        string="Immatriculation",
        required=True
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
