# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Esis_digitalCategorie(models.Model):
    _name = 'esis_digital.categorie'
    _description = 'Gestion des categories'

    name = fields.Char(string='Liste des categories')
    materiel_ids = fields.One2many(comodel_name='esis_digital.materiel',
                                   inverse_name='categorie_id',
                                   string='materiels de la categorie')
