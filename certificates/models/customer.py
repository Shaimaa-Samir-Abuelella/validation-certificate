from odoo import models, fields, api
from odoo import exceptions


class Customer(models.Model):
    _inherit = "res.partner"
