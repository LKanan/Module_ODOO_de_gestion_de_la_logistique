# -*- coding: utf-8 -*-
# from odoo import http


# class Esis-digital(http.Controller):
#     @http.route('/esis-digital/esis-digital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esis-digital/esis-digital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('esis-digital.listing', {
#             'root': '/esis-digital/esis-digital',
#             'objects': http.request.env['esis-digital.esis-digital'].search([]),
#         })

#     @http.route('/esis-digital/esis-digital/objects/<model("esis-digital.esis-digital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esis-digital.object', {
#             'object': obj
#         })
