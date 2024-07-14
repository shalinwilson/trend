# -*- coding: utf-8 -*-
# from odoo import http


# class TredlineMain(http.Controller):
#     @http.route('/tredline_main/tredline_main', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tredline_main/tredline_main/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tredline_main.listing', {
#             'root': '/tredline_main/tredline_main',
#             'objects': http.request.env['tredline_main.tredline_main'].search([]),
#         })

#     @http.route('/tredline_main/tredline_main/objects/<model("tredline_main.tredline_main"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tredline_main.object', {
#             'object': obj
#         })

