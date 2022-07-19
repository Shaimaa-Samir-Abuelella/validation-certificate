from odoo import models, fields, api
from odoo import exceptions


class CarBrand(models.Model):
    _name = "iti.certificate.carbrand"
    _description = ""

    cerificate_id = fields.One2many(comodel_name="iti.certificate.certificates", inverse_name="car_brand")
    brand_name = fields.Char()
    _rec_name = "brand_name"