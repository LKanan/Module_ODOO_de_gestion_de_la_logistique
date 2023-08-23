# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Esis_digitalEffect_dmd(models.Model):
    _name = 'esis_digital.effect_dmd'
    _description = 'Gestion des demandes effectuées'
    _rec_name = 'state_request'
    # _inherit = 'mail.thread'
    # nom_SGAD = "Patient"
    # email = "elkanan10@gmail.com"

    create_uid = fields.Many2one('res.users', string='Demande faite par', readonly=True)
    # date_0f_Request
    create_date = fields.Datetime(string="Date de la demande", readonly=True)
    state_request = fields.Selection([
        ('Déja approuvée', 'Approuvé'),
        ('Pas encore approuvée', 'Non approuvé'),
    ],
        string="Approbation",
        default='Pas encore approuvée')
    need_ids = fields.One2many(comodel_name='esis_digital.needs',
                               inverse_name='effect_dmd_id',
                               string='Liste des besoins')
    montant_total = fields.Integer(string='Cout total', default=0)

    # @api.onchange('need_ids')
    # def reunitialisation(self):
    #     if self.need_ids:
    #         self.montant_total = 0
    # @api.depends('need_ids')
    # def sommation_totale(self):
    #     # for materiel in self:
    #     #     materiel.total_price = str(materiel.quantity * materiel.unit_price) + ' FC'
    #     if self.need_ids:
    #         prix_tot_unitaires = self.env['esis_digital.needs'].search([], limit=None)
    #         for prix in prix_tot_unitaires:
    #             self.montant_total += (prix.quantity * prix.unit_price)
