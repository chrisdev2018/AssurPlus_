# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Genre(models.Model):
    _name = 'assurplus.genre'
    _description = 'Genre'
    
    code = fields.Char(
        string='Code'
    )
    
    name = fields.Char(
        string='Genre'
    )
    