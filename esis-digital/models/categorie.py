# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Esis_digitalCategorie(models.Model):
    _name = 'esis_digital.categorie'
    _description = 'Gestion des categories'

    name = fields.Char(string='Liste des categories')
    materiel_id = fields.Many2one('esis_digital.materiel')
