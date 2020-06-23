from odoo import api, models


class COAReport(models.AbstractModel):
    """ Model to contain the information related to printing the information about
    the COA report"""

    _name = "report.specs_report_website.report_coa_template"

    @api.model
    def _get_report_values(self, docids, data=None):
        """Get the report values.
                        :param : model
                        :param : docids
                        :param : data
                        :return : data
                        :return : Product template records"""
        lot_serial_no = self.env['stock.production.lot'].browse(docids)
        return {
            'data': data,
            'docs': lot_serial_no
        }