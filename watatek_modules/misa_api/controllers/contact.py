from odoo import http
from odoo.http import request
import json
import requests
from ..apps.crm.mapping.contact import MisaContact


class ContactController(http.Controller):

    _login_info = {}
    _contact_info = {}

    def _get_misa_token(self):
        url = "https://crmconnect.misa.vn/api/v2/Account"
        headers = {
            'Content-Type': 'application/json',
        }
        body = {
            "client_id": "d516a1498f56f6ca8f001045b92687fe",  # app id CRM misa
            "client_secret": "yBM+ifggqFeg9hj9AKXl5ilGbvN8fNLR5aEVeb8IjkU="  # Mã bảo mật misa CRM
        }

        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            data = response.json()
            self._login_info = data
        else:
            self._login_info = {}

    def get_all_contact_info(self):
        url = 'https://crmconnect.misa.vn/api/v2/Contacts'
        headers = {
            'Authorization': 'Bearer ' + self._login_info.get('data', ''),
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self._contact_info = data
        else:
            self._contact_info = {}

    def get_contact_odoo(self):
        partner = request.env['res.partner'].search([])
        partner_json = partner.read()
        return partner_json



    @http.route('/misa/createdata', auth='public', type='http', website=True)
    def create_misa_contact(self):
        url = 'https://crmconnect.misa.vn/api/v2/Contacts'
        headers = {
            'Authorization': 'Bearer ' + self._login_info.get('data', ''),
            'Content-Type': 'application/json',
        }
        partners = self.get_contact_odoo()

        misa_contacts = []
        for partner in partners:
            misa_contact = MisaContact.convert_partner_to_misa_contact(partner)
            # Convert misa_contact to a dictionary if it's not already one
            if hasattr(misa_contact, '__dict__'):
                misa_contacts.append(misa_contact.__dict__)
            else:
                misa_contacts.append(misa_contact)

        # Pass the list of dictionaries directly to the `json` parameter
        response = requests.post(url, headers=headers, json=misa_contacts)
        
        if response.status_code == 200:
            return request.make_response(response.text, [('Content-Type', 'application/json')])
        else:
            return request.make_response(json.dumps({'error': 'Unable to create data: ' + str(response.status_code)}), [('Content-Type', 'application/json')])













    @http.route('/misa/login', auth='public', type='http', website=True)
    def misa_login(self):
        self._get_misa_token()
        if self._login_info:
            return request.make_response(json.dumps(self._login_info), [('Content-Type', 'application/json')])
        else:
            return request.make_response(json.dumps({'error': 'Unable to fetch data'}), [('Content-Type', 'application/json')])

    @http.route('/misa/contact', type='http', auth='user', methods=['GET'], csrf=False)
    def get_all_misa_data(self):
        if not self._login_info:
            self._get_misa_token()
        if self._login_info:
            self.get_all_contact_info()
            return request.make_response(json.dumps(self._contact_info), [('Content-Type', 'application/json')])
        else:
            return request.make_response(json.dumps({'error': 'Token not available'}), [('Content-Type', 'application/json')])
