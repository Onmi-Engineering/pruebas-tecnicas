from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    campo1 = fields.Char('Nombre del campo')
