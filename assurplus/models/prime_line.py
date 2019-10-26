# -*- coding: utf-8 -*-
from odoo import api, models, fields

class PrimeLine(models.Model):
    _name = "assurplus.prime_line"

    prime_id = fields.Many2one(
        string="Prime",
        comodel_name="assurplus.prime"
    )
    
    conditions_id = fields.Many2one(
        comodel_name='assurplus.conditions_parti',
         string='Conditions Particulieres')
    

    val = fields.Selection(
        string="Val",
        selection=[
            (0, 'OUI'),
            (1, 'NON')
        ]
    )

    garantie = fields.Char(
        string="Limite de garantie"
    )

    montant = fields.Integer(
        string="Montant"
    )

    reduction = fields.Float(
        string="Réduction"
    )

    majoration = fields.Float(
        string="Majoration"
    )

    comptant = fields.Integer(
        string="Prime Comptant",
        compute="_calcul_comptant"
    )

    @api.multi
    def _calcul_comptant(self):
        return True