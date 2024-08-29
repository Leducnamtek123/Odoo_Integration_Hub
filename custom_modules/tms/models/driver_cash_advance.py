from odoo import models, fields

class DriverCashAdvance(models.Model):
    _name = 'tms.driver.cash.advance'
    _description = 'Driver Cash Advance'

    name = fields.Char(string='Reference', required=True)
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid'),
        ('cancel', 'Cancelled'),
    ], default='draft', string='Status')
