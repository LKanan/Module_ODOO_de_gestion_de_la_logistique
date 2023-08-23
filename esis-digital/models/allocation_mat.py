# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Esis_digitalAllocation(models.Model):
    _name = 'esis_digital.allocation_mat'
    _description = 'Gestion des allocations materiel'
    _rec_name = 'materiel_id'

    materiel_id = fields.Many2one(comodel_name='esis_digital.materiel', string='Description')
    categorie_id = fields.Many2one(comodel_name='esis_digital.categorie', required=True)
    quantity = fields.Integer(string='Quantité')
    motif = fields.Char()
    attachment = fields.Char(string="Pièce jointe ")
    allocation_id = fields.Many2one(comodel_name='esis_digital.allocation')

    create_uid = fields.Many2one('res.users', string='Allocation faite par', readonly=True)
    # date_0f_Request
    create_date = fields.Datetime(string="Date de l'allocation", readonly=True)

    # id = fields.Integer(string="ID", readonly=True)

    """Alors on comprend que pour modifier ou atteindre la valeur d'un certain enregistrement de n'importe que model et
    dans n'importe quel model on utilise le decorateur on change et puis on lui specifie les champs sur lequel on garde
     un oeil, si ces chaamps passés en parametre du decorateur on change varie alors on va executer la foction qui vient 
     juste apres le decorateur.
     Ex:@api.onchange('quantity', 'categorie_id')
     
     Mais on constate aussi que pour que maintenant la fonction qui doit s'executer reconnaisse ou qu'il soit aussi 
      sensible aux variations des champs placés en paramettre du decorateur onchange il faut le specifier dans la condition
      de test de variation qui se trouve à l'interieur, sinon il ne fera rien en cas e changement de valeur d'un champ 
      voulu.
      Ex: if self.quantity or self.categorie_id:
      """

    """Pour le decorateur @api.constrains c'est presque la meme chose seulement lui s'execute pour detecter des contraintes
    et ici il est utilisé pour detecter le manque des materiels dans la base de données pour eviter de permettre une commande
    alors que les materiels sont deja finis"""

    @api.constrains('quantity', 'categorie_id', 'materiel_id')
    def check_quantity_materiels(self):
        if self.quantity or self.categorie_id or self.materiel_id:
            materiel_list = self.env['esis_digital.materiel'].search([], limit=None)
            for materiel in materiel_list:
                ancienne_valeur = materiel.quantity

                if materiel.quantity == 0:
                    raise ValidationError(f"""Désolé! La quantité en stock est vide.""")

                elif materiel.quantity < self.quantity:
                    raise ValidationError(f"""Désolé!
La quantité spécifiée est supérieure à la quantité en stoc.
Quantité en stock = {ancienne_valeur} materiel(s), quantité spécifiée = {self.quantity} materiels.""")

                elif (materiel.name == self.materiel_id.name) and (materiel.categorie_id == self.categorie_id):
                    # ancienne_valeur = materiel.quantity
                    if materiel.quantity >= self.quantity:
                        materiel.quantity = materiel.quantity - self.quantity
                        return {'warning': {'title': 'Succes', 'message': 'Allocation effectuée'}}
