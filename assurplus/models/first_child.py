# -*- coding: utf-8 -*-
from odoo import api, fields, models

class FirstChild(models.Model):
    _name = "assurplus.first_child"

    name = fields.Char(
        string="Model 1"
    )
    champ_test = fields.Char(
        string="Champ test :",
        default="Un texte juste comme ça",
        readonly=True
    )