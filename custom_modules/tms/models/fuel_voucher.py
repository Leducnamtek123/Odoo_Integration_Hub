from odoo import models, fields

class FuelVoucher(models.Model):
    _name = 'tms.fuel.voucher'
    _description = 'Fuel Voucher'

    name = fields.Char(string='Voucher Number', required=True)
    amount = fields.Float(string='Amount', required=True)
    voucher_date = fields.Date(string='Voucher Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('cancelled', 'Cancelled'),
    ], default='draft', string='Status')
