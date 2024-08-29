from odoo import models, fields

class Kits(models.Model):
    _name = 'tms.kits'
    _description = 'Kits'

    name = fields.Char(string='Kit Name', required=True)
    description = fields.Text(string='Description')
    quantity = fields.Integer(string='Quantity', required=True)
    location = fields.Char(string='Location')
