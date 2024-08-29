from odoo import models, fields

class FreightInvoicing(models.Model):
    _name = 'tms.freight.invoicing'
    _description = 'Freight Invoicing'

    name = fields.Char(string='Invoice Number', required=True)
    amount = fields.Float(string='Amount', required=True)
    invoice_date = fields.Date(string='Invoice Date', required=True)
    truck_id = fields.Many2one('fleet.vehicle', string='Truck')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
    ], default='draft', string='Status')
