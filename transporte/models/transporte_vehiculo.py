from odoo import fields, models


class TransporteVehiculo(models.Model):
    _name = 'transporte.vehiculo'
    _description = 'Vehículo'

    name = fields.Char('Nombre')
