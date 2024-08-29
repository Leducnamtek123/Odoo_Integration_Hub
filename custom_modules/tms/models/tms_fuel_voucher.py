from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TmsFuelVoucher(models.Model):
    _name = 'tms.fuel.voucher'
    _description = 'Fuel Voucher'

    date = fields.Date(string='Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    vendor_id = fields.Many2one('res.partner', string='Vendor', required=True)
    notes = fields.Text(string='Notes')

    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount <= 0:
                raise ValidationError("The amount must be positive.")
