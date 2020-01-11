# -*- coding: utf-8 -*-
from odoo import api, fields, models


list_cat = [('01', '01'), ('02', '02'), ('03', '03'), ('04_A', '04/A'), ('04_B', '04/B'),
            ('04_C', '04/C'), ('05_A', '05/A'), ('05_B', '05/B'), ('06', '06'), ('07', '07'),
            ('08', '08'), ('09', '09'), ('10', '10')
            ]


class Vehicule(models.Model):
    _name = "assurplus.vehicule"
    
    name = fields.Char(
        string="Immatriculation",
        required=True
    )
    
    categorie = fields.Selection(
        string='', 
        selection=list_cat
    )
    

    # TODO: mettre une contrainte sql pour le name

    usage = fields.Char(
        string="Usage",
        readonly=True
    )
    
    genre = fields.Many2one(
        comodel_name='assurplus.genre',
        string='Genre',
        domain="[('code', '=', categorie)]"
    )
    

    marque = fields.Char(
        string="Marque"
    )

    chassis = fields.Char(
        string="N° Chassis",
        required=True
    )

    # TODO: mettre une contrainte sql pour le name

    zone = fields.Selection(
        string="Zone de circulation",
        selection=[('A', 'A'), ('B', 'B'), ('C', 'C')]
    )    

    puissance = fields.Integer(
        string="Puissance (en CV)"
    )

    source = fields.Selection(
        string="Source d'energie",
        selection=[
            ('ess', 'Essence'),
            ('gas', 'Gasoil'),
            ('elec', 'Electrique')
        ]
    )

    nb_place = fields.Integer(
        string="Nombre de places"
    )
    
    @api.onchange('categorie')
    def _onchange_categorie(self):
        for rec in self:
            if rec.categorie:
                rec.usage = "CAT-" + rec.categorie.replace('_', '/')
            else:
                rec.usage = ""