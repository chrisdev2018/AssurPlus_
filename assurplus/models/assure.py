# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Assure(models.Model):
    _name = "assurplus.assure"

    name = fields.Char(
        string="nom",
        required=True
    )
    prenom = fields.Char(
        string="Prénom",
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
