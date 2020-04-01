# -*- coding: utf-8 -*-
import json
import logging
from werkzeug.exceptions import Forbidden, NotFound

from odoo import fields, http, tools, _
from odoo.http import request
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.website.controllers.main import QueryURL
from odoo.exceptions import ValidationError
from odoo.addons.website.controllers.main import Website
from odoo.addons.sale.controllers.product_configurator import ProductConfiguratorController
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.osv import expression
_logger = logging.getLogger(__name__)


class ProductSpecsReport(ProductConfiguratorController):

    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def productspecsreport(self):
        print()

    def product(self, product, category='', search='', **kwargs):
        if not product.can_access_from_current_website():
            raise NotFound()

        add_qty = int(kwargs.get('add_qty', 1))

        product_context = dict(request.env.context, quantity=add_qty,
                               active_id=product.id,
                               partner=request.env.user.partner_id)
        ProductCategory = request.env['product.public.category']

        if category:
            category = ProductCategory.browse(int(category)).exists()

        attrib_list = request.httprequest.args.getlist('attrib')
        attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        attrib_set = {v[1] for v in attrib_values}

        keep = QueryURL('/shop', category=category and category.id, search=search, attrib=attrib_list)

        categs = ProductCategory.search([('parent_id', '=', False)])

        pricelist = request.website.get_current_pricelist()

        def compute_currency(price):
            return product.currency_id._convert(price, pricelist.currency_id,
                                                product._get_current_company(pricelist=pricelist,
                                                                             website=request.website),
                                                fields.Date.today())

        if not product_context.get('pricelist'):
            product_context['pricelist'] = pricelist.id
            product = product.with_context(product_context)

        values = {
            'search': search,
            'category': category,
            'pricelist': pricelist,
            'attrib_values': attrib_values,
            # compute_currency deprecated, get from product
            'compute_currency': compute_currency,
            'attrib_set': attrib_set,
            'keep': keep,
            'categories': categs,
            'main_object': product,
            'product': product,
            'add_qty': add_qty,
            'optional_product_ids': [p.with_context({'active_id': p.id}) for p in product.optional_product_ids],
            # get_attribute_exclusions deprecated, use product method
            'get_attribute_exclusions': self._get_attribute_exclusions,
        }
        return request.render("website_sale.product", values)
