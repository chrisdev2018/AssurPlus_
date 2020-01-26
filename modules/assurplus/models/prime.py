# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Prime(models.Model):
    _name = "assurplus.prime"

    name = fields.Char(
        string = "Libellé", 
        required = True
    )
    


