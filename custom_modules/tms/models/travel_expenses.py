from odoo import models, fields

class TravelExpenses(models.Model):
    _name = 'tms.travel.expenses'
    _description = 'Travel Expenses'

    name = fields.Char(string='Description', required=True)
    amount = fields.Float(string='Amount', required=True)
    expense_date = fields.Date(string='Expense Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='draft', string='Status')
