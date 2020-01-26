# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Conducteur(models.Model):
    _name = 'assurplus.conducteur'
    _description = 'Conducteur'
    
    name = fields.Char(
        string='Nom & Prénom'
    )
    
    cat_permis = fields.Selection(
        selection=[
            ('A', 'A'),  ('B', 'B'),  ('C', 'C'),  ('D', 'D'),  ('E', 'E'),
             ('F', 'F'),  ('G', 'G'),  ('H', 'H'),
        ],        
        string='Cat permis de conduire'
    )
    
    sexe = fields.Selection(
        string='Sexe',
         selection=[('M', 'Masculin'),
                     ('F', 'Féminin'),]
    )
        
    num_permis = fields.Char(
        string='Numéro du permis'
    )
    
    delivre = fields.Date(
        string='Délivré le'
    )
    
    a_ = fields.Char(
        string='A (ville d\'obtention du permis)'
    )
    
    