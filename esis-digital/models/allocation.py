# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Esis_digitalAllocation(models.Model):
    _name = 'esis_digital.allocation'
    _description = 'Gestion des informations sur celui qui alloue'
    _rec_name = 'etat_remise'

    # Materiel donné à:
    given_to = fields.Char(string="Demandeur (nom & Post_nom)", required=True)
    matricule = fields.Char(required=True)
    # date de livraison
    create_date = fields.Datetime(string="Date d'allocation", readonly=True)
    # variable qui enregistre toutes les dates de modifications ou de mise à jour ou de suppression
    write_date = fields.Datetime(string="Date de modification", readonly=True)
    # Variable qui enregistre la date prevue pour la remise du materiel
    delivery_date = fields.Date(string='Date de remise', required=True)
    # petite description des materiels donnés
    commentaires = fields.Text()
    create_uid = fields.Many2one('res.users', string='Donneur', readonly=True)
    # Variable pour signifier la remise ou la non remise du materiel
    etat_remise = fields.Selection([('Déjà remis', 'Remis'), ('Pas encore remis', 'Non remis')],
                                   string="Etat de remise", default='Pas encore remis')
    # Variable pour recuperer la liste des materiels pris
    alloc_mat_ids = fields.One2many(comodel_name='esis_digital.allocation_mat',
                                    inverse_name='allocation_id',
                                    string='Materiels')

    # id = fields.Integer(string="ID", readonly=True)

