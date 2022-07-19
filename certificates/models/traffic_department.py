from odoo import models, fields, api
from odoo import exceptions


class TrafficDepartment(models.Model):
    _name = "iti.certificate.trafficdepartment"
    _description = ""

    cerificate_id = fields.One2many(comodel_name="iti.certificate.certificates", inverse_name="traffic_department")
    Department_name = fields.Char()