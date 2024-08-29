from odoo import models, fields

class TravelEvents(models.Model):
    _name = 'tms.travel.events'
    _description = 'Travel Events'

    name = fields.Char(string='Event Description', required=True)
    event_date = fields.Date(string='Event Date', required=True)
    truck_id = fields.Many2one('fleet.vehicle', string='Truck')
    event_type = fields.Selection([
        ('arrival_delay', 'Arrival Delay'),
        ('missing_cargo', 'Missing Cargo'),
        ('accident', 'Accident'),
        ('other', 'Other'),
    ], string='Event Type')
    notes = fields.Text(string='Notes')
