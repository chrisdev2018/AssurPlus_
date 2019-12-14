# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Assure(models.Model):
    _name = "assurplus.assure"

    name = fields.Char(
        string="Nom & Prénom",
        required=True
    )
    
    tel = fields.Char(
        string="Téléphone"
    )

    ville = fields.Char(
        string="Ville"
    )

    activite = fields.Char(
        string="Activité"
    )

    profession = fields.Char(
        string="Profession"
    )
    
    test_button = fields.Integer(
        string='Contrats',
        default=1)
    
    @api.multi
    def open_conditions_parti(self):
        raise ValidationError('Test Réussi!!!!')