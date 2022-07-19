from odoo import models, fields, api
from odoo import exceptions


class CertificateType(models.Model):
    _name = "iti.certificate.type"
    _description = ""

    cerificate_id = fields.One2many(comodel_name="iti.certificate.certificates", inverse_name="certificate_types")
    certificate_type = fields.Char()