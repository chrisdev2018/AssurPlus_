# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Usage(models.Model):
    _name = 'assurplus.usage'
    _description = 'description'
    _rec_name = 'usage'
    
    code = fields.Char(
        string='Code'
    )
    
    usage = fields.Char(
        string='Usage'
    )
    