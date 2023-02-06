from odoo import models, fields, api


class estateProperty(models.Model):
    _inherit = 'estate.property'

    def button_sold(self):
        print('hello every body')
        return super().button_sold()