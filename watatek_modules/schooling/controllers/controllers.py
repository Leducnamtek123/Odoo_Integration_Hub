# -*- coding: utf-8 -*-
from odoo import http


class Schooling(http.Controller):
    @http.route('/schooling/schooling', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/schooling/schooling/objects', auth='public')
    def list(self, **kw):
        return http.request.render('schooling.listing', {
            'root': '/schooling/schooling',
            'objects': http.request.env['schooling.schooling'].search([]),
        })

    @http.route('/schooling/schooling/objects/<model("schooling.schooling"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('schooling.object', {
            'object': obj
        })

