import base64
from collections import OrderedDict

from odoo import http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.tools import image_resize_image
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import pager as portal_pager, CustomerPortal
from odoo.addons.web.controllers.main import Binary

class CustomerPortal(CustomerPortal):

    def _lot_serial_no_get_page_view_values(self, lot, access_token, **kwargs):
        #
        def resize_to_48(b64source):
            if not b64source:
                b64source = base64.b64encode(Binary().placeholder())
            return image_resize_image(b64source, size=(48, 48))

        values = {
            'lot': lot,
            'resize_to_48': resize_to_48,
        }
        return self._get_page_view_values(lot, access_token, values,'my_lot_history', True, **kwargs)


    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()
        values['lot_count'] = request.env['stock.production.lot'].search_count([
            ('purchase_order_count', '!=', 0)
        ])
        return values


    @http.route(['/my/purchased/lots', '/my/purchased/lots/page/<int:page>'], type='http', auth="user", website=True)
    def portal_lots_purchased(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        Lot_Serial_No = request.env['stock.production.lot']

        domain = []

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc, id desc'},
            'name': {'label': _('Name'), 'order': 'name asc, id asc'},
        }
        # default sort by value
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        # default filter by value
        if not filterby:
            filterby = 'all'

        # count for pager
        lot_count = Lot_Serial_No.search_count(domain)
        # make pager
        pager = portal_pager(
            url="/my/purchased/lots",
            url_args={'date_begin': date_begin, 'date_end': date_end},
            total=lot_count,
            page=page,
            step=self._items_per_page
        )
        # search the purchase orders to display, according to the pager data
        lots = Lot_Serial_No.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager['offset']
        )

        request.session['my_lot_history'] = lots.ids[:100]


        values.update({
            'date': date_begin,
            'lots': lots,
            'page_name': 'lots_purchased',
            'pager': pager,
            'sortby': sortby,
            'filterby': filterby,
            'default_url': '/my/purchased/lots',
        })
        return request.render("specs_report_website.portal_my_purchased_lots", values)


    @http.route(['/my/purchased/lots<int:lot_id>'], type='http', auth="public", website=True)
    def portal_my_purchased_lot(self, lot_id=None, access_token=None, **kw):
        try:
            lot_sudo = self._document_check_access('stock.production.lot', lot_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        values = self._lot_serial_no_get_page_view_values(lot_sudo, access_token, **kw)

        return request.render("specs_report_website.portal_my_purchased_lot", values)