# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Esis_digitalNeeds(models.Model):
    _name = 'esis_digital.needs'
    _description = 'Gestion des etats de besoins'
    _rec_name = 'object'

    object = fields.Char(string='Objet')
    imputation = fields.Char()
    description = fields.Text()
    reference = fields.Char()
    quantity = fields.Integer(string='Quantité')
    unit_price = fields.Float(string='Pix unitaire en FC')
    # Compute comme attribut prend comme valeur le nom de la foncalloc_mat_idstion qui va effectuer des traitement sur ce champ
    total_price = fields.Char(string='Prix total', compute='compute_resultat')
    create_uid = fields.Many2one('res.users', string='Fait par', readonly=True)
    effect_dmd_id = fields.Many2one(comodel_name='esis_digital.effect_dmd')
    create_date = fields.Datetime(string="Date de la demande", readonly=True)


    """ Avec cette methode je peux faire des operations sur les valeurs des champs et là on vient de définir une opération
    de multiplication de la quantité par le prix unitaire pour trouver le prix total"""

    @api.depends('quantity', 'unit_price')
    def compute_resultat(self):
        for materiel in self:
            materiel.total_price = str(materiel.quantity * materiel.unit_price) + ' FC'
