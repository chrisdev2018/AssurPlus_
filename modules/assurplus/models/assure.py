# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Assure(models.Model):
    _name = "assurplus.assure"
    
    _description = "Test description"

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
    
    count_contrats = fields.Integer(
        string='Contrats',
        compute='get_count_contrats')
    
    count_cars = fields.Integer(
        compute='get_count_cars', 
        string='Véhicules')
    
    
    @api.multi
    def open_conditions_parti(self):
        return {
            'name': ('Conditions Particulières'),
            'domain': [('assure_id', '=', self.id)],
            'view_type': 'form',
            'view_id': False,
            'res_model': 'assurplus.conditions_parti',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
        
    def get_count_contrats(self):
        count = self.env['assurplus.conditions_parti'].search_count([('assure_id', '=', self.id)])
        self.count_contrats = count 
        
    def get_count_cars(self):
        count = self.env['assurplus.vehicule'].search_count([('conducteur', '=', self.id)])
        self.count_cars = count
        
    def open_vehicules(self):
        return {
            'name': ('Véhicules'),
            'domain': [('conducteur', '=', self.id)],
            'view_type': 'form',
            'view_id': False,
            'res_model': 'assurplus.vehicule',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }    
    