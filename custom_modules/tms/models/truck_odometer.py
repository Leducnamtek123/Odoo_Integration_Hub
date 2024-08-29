from odoo import models, fields

class TruckOdometer(models.Model):
    _name = 'tms.truck.odometer'
    _description = 'Truck Odometer'

    truck_id = fields.Many2one('fleet.vehicle', string='Truck', required=True)
    odo_reading = fields.Float(string='Odometer Reading', required=True)
    reading_date = fields.Date(string='Reading Date', required=True)
    notes = fields.Text(string='Notes')
