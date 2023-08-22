# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Esis_digitalMateriel(models.Model):
    _name = 'esis_digital.materiel'
    _description = 'Gestion des materiels'

    name = fields.Char(required=True, string='Nom materiel')
    categorie_id = fields.Many2one(comodel_name='esis_digital.categorie', required=True)
    num_serie = fields.Char(string='Numéro de série', required=True)
    quantity = fields.Integer(string='Quantité')
    # registration_date
    create_date = fields.Datetime(string="Date d'enregistrement", readonly=True)
    # user_id
    create_uid = fields.Many2one('res.users', string='Enregistré par', readonly=True)
    write_date = fields.Datetime(string="Date de modification", readonly=True)

    # id_cat
