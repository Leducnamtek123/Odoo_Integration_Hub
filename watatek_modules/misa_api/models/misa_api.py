import requests
from odoo import models, fields, api
from ..apps.crm.mapping.contact import MisaContact
from odoo import http
from odoo.http import request
import json

class MisaApi(models.Model):
    _name = 'misa.api.action'
    _description = 'MISA API Action'
    name_api = fields.Char(string='Name Api', required=True)
    client_id = fields.Char(string='Client ID', required=True)
    client_secret = fields.Char(string='Client Secret', required=True)
    
    def _misa_login(self):
        url = "https://crmconnect.misa.vn/api/v2/Account"
        headers = {
            'Content-Type': 'application/json',
        }
        body = {
            "client_id": self.client_id,  # app id CRM misa
            "client_secret": self.client_secret  # Mã bảo mật misa CRM
        }
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            data = response.json()
            return data.get("data")
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
        
    
    def _create_misa_contact(self, partners, token):
        url = 'https://crmconnect.misa.vn/api/v2/Contacts'
        
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json',
        }
        
        misa_contacts = []
        for partner in partners:
            misa_contact = MisaContact.convert_partner_to_misa_contact(partner)
            if hasattr(misa_contact, '__dict__'):
                misa_contacts.append(misa_contact.__dict__)
            else:
                misa_contacts.append(misa_contact)

        response = requests.post(url, headers=headers, json=misa_contacts)
        
        if response.status_code == 200:
            # Trả về nội dung JSON hoặc văn bản từ response
            return response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
        else:
            return {'error': 'Unable to create data: ' + str(response.status_code)}