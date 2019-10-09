# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Prime(models.Model):
    _name = "assurplus.prime"

    name = fields.Char(
        string="Libellé",
        required=True
    )

    valeur = fields.Float(
        string="Valeur"
    )

    garantie = fields.Char(
        string="Limite de garantie"
    )

    reduction = fields.Float(
        string="Réduction(%)"
    )

    majoration = fields.Float(
        string="Majoration(%)"
    )

    comptant = fields.Float(
        string="Comptant",
        compute="calcul_comptant",
        store=True,
        readonly=True
    )

    @api.multi
    def calcul_comptant(self):
        for rec in self:
            return True

