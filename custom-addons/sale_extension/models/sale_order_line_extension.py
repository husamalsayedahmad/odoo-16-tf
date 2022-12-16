from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    total_weight = fields.Float(string='#Weight')
    total_volume = fields.Float(string='#Volume')

    @api.onchange('product_uom_qty')
    def onchange_total_weight(self):
        self.total_weight = self.product_id.weight * self.product_uom_qty

    @api.onchange('product_uom_qty')
    def onchange_number_of_boxes(self):
        self.total_volume = self.product_id.volume * self.product_uom_qty



