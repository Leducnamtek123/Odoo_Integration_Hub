from odoo import models, fields

class TruckRedTapes(models.Model):
    _name = 'tms.truck.red.tapes'
    _description = 'Truck Red Tapes'

    name = fields.Char(string='Red Tape Reference', required=True)
    truck_id = fields.Many2one('fleet.vehicle', string='Truck')
    description = fields.Text(string='Description')
    date_issued = fields.Date(string='Date Issued')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('resolved', 'Resolved'),
        ('pending', 'Pending'),
    ], default='draft', string='Status')
