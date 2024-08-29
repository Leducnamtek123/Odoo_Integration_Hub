from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TmsDriver(models.Model):
    _name = 'tms.driver'
    _description = 'Driver'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    license_number = fields.Char(string='License Number', required=True)
    contact_number = fields.Char(string='Contact Number')
    active = fields.Boolean(string='Active', default=True)

    @api.constrains('license_number')
    def _check_license_number(self):
        for record in self:
            if len(record.license_number) < 6:
                raise ValidationError("The license number must be at least 6 characters long.")
