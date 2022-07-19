from odoo import models, fields, api
from odoo import exceptions


class TrafficDepartment(models.Model):
    _name = "iti.certificate.trafficdepartment"
    _description = ""

    cerificate_id = fields.One2many(comodel_name="iti.certificate.certificates", inverse_name="traffic_department")
    department_name = fields.Char()
    _rec_name = "department_name"