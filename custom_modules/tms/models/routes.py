from odoo import models, fields, api

class TmsRoutes(models.Model):
    _name = 'tms.routes'
    _description = 'Routes'

    name = fields.Char(string='Route Name')
    start_place_id = fields.Many2one('tms.places', string='Start Place')
    end_place_id = fields.Many2one('tms.places', string='End Place')
    distance = fields.Float(string='Distance')
    estimated_time = fields.Float(string='Estimated Time')
    google_maps_url = fields.Char(string='Google Maps URL', compute='_compute_google_maps_url', store=True)

    @api.depends('start_place_id', 'end_place_id')
    def _compute_google_maps_url(self):
        for record in self:
            if record.start_place_id and record.end_place_id:
                start_lat = record.start_place_id.latitude
                start_lng = record.start_place_id.longitude
                end_lat = record.end_place_id.latitude
                end_lng = record.end_place_id.longitude
                record.google_maps_url = f'https://www.google.com/maps/dir/{start_lat},{start_lng}/{end_lat},{end_lng}'
            else:
                record.google_maps_url = ''
