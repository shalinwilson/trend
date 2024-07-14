# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SupplierInfo(models.Model):
    inherit = "product.supplierinfo"


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        product = super(ProductTemplate, self).create(vals)
        supplierinfo_model = self.env['product.supplierinfo']

        # Assign specific vendor to the new product
        specific_vendor = self.env.ref('tredline_main.specific_vendor')
        supplierinfo_model.create({
            'partner_id': specific_vendor.id,
            'product_tmpl_id': product.id,
            'price': product.list_price # Set your desired price here
        })

        return product