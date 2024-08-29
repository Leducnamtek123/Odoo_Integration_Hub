from dataclasses import dataclass
from datetime import datetime

@dataclass
class MisaContact:
    form_layout: str
    contact_code: str
    contact_name: str
    mobile: str
    other_phone: str
    email: str
    account_type : str # Loại liên hệ invividual, company
    mailing_province: str #city
    mailing_street: str #street
    mailing_zip : str

    def convert_partner_to_misa_contact(partner):
        return MisaContact(
            account_type="",
            form_layout='Mẫu tiêu chuẩn',
            contact_code="",
            contact_name=partner.get('name', ''),
            mobile=partner.get('phone_sanitized', ''),
            other_phone=partner.get('phone_sanitized', ''),
            email=partner.get('email', ''),
            mailing_province="",
            mailing_street=partner.get('street', ''),
            mailing_zip=partner.get('zip', ''),
        )

    def convert_misa_contact_to_partner(misa_contact):
        partner = {
            'is_company': misa_contact.account_type == 'company',
            'name': misa_contact.contact_name,
            'function': misa_contact.title,
            'phone_sanitized': misa_contact.mobile,
            'email': misa_contact.email,
            'city': misa_contact.mailing_province,
            'street': misa_contact.mailing_street,
            'zip': misa_contact.mailing_zip,
        }
    
        return partner
