from odoo import models, api
import json

class IrActionsServer(models.Model):
    _inherit = 'ir.actions.server'
    
    @api.model
    def _run_action_misa_api(self):
        active_id = self.env.context.get('active_id')
        if not active_id:
            print("No active partner found.")
            return
        partner = self.env['res.partner'].browse(active_id)
        if not partner.exists():
            print("Partner not found.")
            return
        partner_data = partner.read()[0]
        misa_action = self.env['misa.api.action'].search([], limit=1)
        token = misa_action._misa_login()
        if token:
            result = misa_action._create_misa_contact([partner_data], token)
            print(f"Result of _create_misa_contact: {result}")