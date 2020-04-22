# -*- coding: utf-8 -*-
import logging

from odoo import fields, http, tools, _
from odoo.http import request

_logger = logging.getLogger(__name__)


class ProductSpecsReport(http.Controller):

    @http.route(['/report/pdf/catalogue_download'], type='http', auth='public')
    def product_specs_report(self, product_id):
        """In this function we are calling the report template
        of the corresponding product and
        downloads the product specification in pdf format"""
        pdf, _ = request.env.ref('specs_report_website.action_report_product_catalog') \
            .sudo().render_qweb_pdf([int(product_id)])
        pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf)),
                          ('Content-Disposition', 'SpecSheet; filename="SpecSheet.pdf"')]
        return request.make_response(pdf, headers=pdfhttpheaders)
