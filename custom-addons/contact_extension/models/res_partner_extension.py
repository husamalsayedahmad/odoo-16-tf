from odoo import models, api, fields
import logging
_logger = logging.getLogger(__name__)

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

    credit_limit = fields.Integer(string='Credit limit', default=0)

    email_groups = fields.Boolean(string='Email Group')

    @api.onchange('preferred_warehouse')
    def change_reference_number(self):
        print(f'the warehouse is', self.preferred_warehouse)
        if self.id != False and self.preferred_warehouse:
            self.ref = f'{self.preferred_warehouse.code}{self.id}'
        else:
            self.ref = ''

    @api.model
    def create(self, values_list):
        print('the values list are' ,values_list)
        return super(ResPartnerExtension, self).create(values_list)

