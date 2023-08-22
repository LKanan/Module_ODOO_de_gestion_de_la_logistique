# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Esis_digitalRapport(models.Model):
    _name = 'esis_digital.rapport'
    _description = 'Gestion des rapports'

    effect_dmd_ids = fields.Many2many(comodel_name='esis_digital.allocation_mat', string='Rapports')
    commentaires = fields.Text()
    create_date = fields.Datetime(string="Date de redaction", readonly=True)

    @api.onchange()
    def send_mail(self):
        self.ensure_one()
        template_id = self.env.ref('esis-digital.email_effect_dmd').id
        ctx = {
            'default_model': 'esis_digital.effect_dmd',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            # 'email_to': self.email,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }
