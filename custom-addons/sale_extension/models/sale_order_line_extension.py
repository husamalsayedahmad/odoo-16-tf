from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    total_weight = fields.Float(string='Total weight')
    total_volume = fields.Float(string='Total volume')
    @api.onchange('product_uom_qty')
    def onchange_total_weight(self):
        print('here', self.product_template_id.weight)
        self.total_weight = self.product_template_id.weight * self.product_uom_qty
    @api.onchange('product_uom_qty')
    def onchange_total_volume(self):
        print('here', self.product_template_id.volume)
        self.total_volume = self.product_template_id.volume * self.product_uom_qty
    # def compute_total_weight(self):
    #     self.onchange_total_weight()
    # def compute_total_volume(self):
    #     self.onchange_total_volume()



