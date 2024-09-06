import json

from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal


class WebsiteEvents(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        user = request.env.user
        if 'purchase_line_count' in counters:
            values['purchase_line_count'] = request.env['purchase.order.line'].sudo().search_count(
                [])
        return values

    @http.route(['/Bidding', '/Bidding/page/<int:page>'], type='http', auth="user", website=True)
    def portal_bidding(self, search=None, search_in='All'):
        """To search the recruitments data in the portal"""
        user = request.env.user
        searchbar_inputs = {
            'All': {'label': 'All', 'input': 'All', 'domain': []},
            'Purchase Order': {'label': 'Purchase Order', 'input': 'Purchase Order',
                               'domain': [('order_id', 'like', search)]},
        }
        search_domain = searchbar_inputs[search_in]['domain']
        order_lines = request.env['purchase.order.line'].sudo().search([
        ])
        search_lines = order_lines.search(search_domain)
        return request.render('purchase_line_portal.portal_my_home_po_lines_views',
                              {
                                  'lines': search_lines,
                                  'page_name': 'bidding',
                                  'search': search,
                                  'search_in': search_in,
                                  'searchbar_inputs': searchbar_inputs
                              })

    @http.route(['/my/purchase_order_line/<int:line_id>'], type='http', auth='user', website=True)
    def portal_purchase_order_line(self, line_id, **kwargs):
        purchase_order_line = request.env['purchase.order.line'].sudo().browse(line_id)
        if not purchase_order_line.exists():
            return request.not_found()

        values = {
            'purchase_order_line': purchase_order_line,
        }
        return request.render('purchase_line_portal.purchase_order_line_template', values)

    @http.route(['/bidding/line/create'], auth='user', type='json', website=True)
    def update_bidding_lines(self, po_id, price):
        bidding_details = request.env['bidding.details'].sudo().search([('po_id', '=', int(po_id))])
        partner = request.env.user.partner_id
        if not bidding_details:
            order_id = request.env['purchase.order'].sudo().search([('id', '=', int(po_id))])
            # todo: to include poline id and product and qty
            bidding = request.env['bidding.details'].sudo().create({
                'po_id': order_id.id,
                'vendor_partner_id': partner.id,
                'bidding_amount': float(price),

            })
        else:
            bidding_details.write({
                'bidding_amount': float(price)
            })
        print(po_id, price)
        return True
