from odoo import api, fields, models
from odoo.exceptions import ValidationError


fulfillment_type_selection = [('warehouse', 'Warehouse'),
                              ('factory/container_Order', 'Factory/Container Order')]
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    override_credit_limit = fields.Boolean(string = 'Override Credit Limit')
    fulfillment_type = fields.Selection(fulfillment_type_selection, default='warehouse')

    def action_confirm(self):
        has_credit_limit_permission = \
            self.env.user.has_group('contact_extension.group_credit_limit')
        if has_credit_limit_permission:
            if (not self.override_credit_limit) and (not self.partner_id.credit_limit != 0):
                raise ValidationError("Credit limit has exceed it's value")
        else:
            if self.partner_id.credit_limit != 0:
                raise ValidationError("Credit limit has exceed it's value")
        return super(SaleOrder, self).action_confirm()








