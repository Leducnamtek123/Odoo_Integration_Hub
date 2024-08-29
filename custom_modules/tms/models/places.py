from odoo import models, fields

class Places(models.Model):
    _name = 'tms.places'
    _description = 'Places'

    name = fields.Char(string='Place Name', required=True)
    latitude = fields.Float(string='Latitude')
    longitude = fields.Float(string='Longitude')
    address = fields.Char(string='Address')
    google_maps_url = fields.Char(string='Google Maps URL', compute='_compute_google_maps_url', store=True)

    def _compute_google_maps_url(self):
        for place in self:
            if place.latitude and place.longitude:
                place.google_maps_url = f"https://www.google.com/maps?q={place.latitude},{place.longitude}"
            else:
                place.google_maps_url = ''
