from odoo import models, fields


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def get_portal_url(self):
        self.ensure_one()
        return '/my/purchase_order_line/%d' % self.id
