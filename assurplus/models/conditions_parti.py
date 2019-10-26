# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime

class ConditionsParti(models.Model):
    _name = "assurplus.conditions_parti"

    name = fields.Char(
        string="Police N°"
    )

    date_effet = fields.Date(
        string="Date Effet"
    )

    date_echeance = fields.Date(
        string="Date Echéance"
    )

    duree = fields.Integer(
        string="Durée"
    )

    avenant = fields.Selection(
        string="Avenant de",
        selection=[
            ('new', 'Nouvelle Affaire')
        ]
    )

    # vehicule
    vehicule_id = fields.Many2one(
        string="Véhicule",
        comodel_namel="assurplus.vehicule",
        required=True
    )

    chassis = fields.Char(
        string="Chassis"
    )

    immat = fields.Char(
        string="Immatriculation"
    )

    # assuré
    assure_id = fields.Many2one(
        string="Assuré",
        comodel_name="assurplus.assure",
        required=True
    )

    prenom = fields.Char(
        string="Prénom"
    )
    
    prime_lines = fields.One2many(
        comodel_name='assurplus.prime_line', 
        inverse_name='conditions_id', 
        string='Primes')
    
    
    @api.depends('date_effet', 'date_echeance')
    def _calcul_duree(self):
        self.duree = 100