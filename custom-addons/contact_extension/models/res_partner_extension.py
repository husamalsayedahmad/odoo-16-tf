from odoo import models, api, fields

preferred_billing_communication_selection = [('by_email', 'By Email'),
                                             ('by_post','By Post')]
account_type_selection = [('credit', 'Credit'), ('cash', 'Cash')]

class ResPartnerExtension(models.Model):
    _inherit = 'res.partner'
    preferred_billing_communication = fields.Selection(preferred_billing_communication_selection,
                                                       string='Preferred Billing Communication')

    account_type = fields.Selection(account_type_selection, string='Account Type')

    preferred_warehouse = fields.Many2one('stock.warehouse', string='Preferred Warehouse')

    email_contacts = fields.Many2many('res.partner','email_tags',
    string='Email Contacts',column1='id', column2="id2")