# -*- coding: utf-8 -*-
# from odoo import http


# class Tms2(http.Controller):
#     @http.route('/tms2/tms2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tms2/tms2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tms2.listing', {
#             'root': '/tms2/tms2',
#             'objects': http.request.env['tms2.tms2'].search([]),
#         })

#     @http.route('/tms2/tms2/objects/<model("tms2.tms2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tms2.object', {
#             'object': obj
#         })

