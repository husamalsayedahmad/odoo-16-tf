from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    total_weight = fields.Float(string='Total weight')
    total_volume = fields.Float(string='Total volume')
    @api.onchange('product_qty')
    def onchange_total_weight(self):
        self.total_weight = self.product_id.product_tmpl_id.weight * self.product_qty
    @api.onchange('product_qty')
    def onchange_total_volume(self):
        self.total_volume = self.product_id.product_tmpl_id.volume * self.product_qty
    # def compute_total_weight(self):
    #     self.onchange_total_weight()
    # def compute_total_volume(self):
    #     self.onchange_total_volume()



