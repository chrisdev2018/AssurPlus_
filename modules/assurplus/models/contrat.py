# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime

class ConditionsParti(models.Model):
    _name = "assurplus.contrat"

    name = fields.Char(
        string="Police N°",
        required=True
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
        comodel_name='assurplus.vehicule',
        string='Véhicule',
        required="True")

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
    
    etat = fields.Selection(
        string='Etat',
         selection=[('open', 'Ouvert'),
                     ('closed', 'Traité')],
         default="open")
    
    @api.multi
    def action_close(self):
        self.etat = "closed"