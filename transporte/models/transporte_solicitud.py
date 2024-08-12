from odoo import fields, models


class TransporteSolicitud(models.Model):
    _name = 'transporte.solicitud'
    _description = 'Solicitud de transporte'

    name = fields.Char('Referencia de transporte')
