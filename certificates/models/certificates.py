from odoo import models, fields, api
from odoo import exceptions
from . import customer
from datetime import date

class Certificates(models.Model):
    _name = "iti.certificate.certificates"
    _description = ""

    # serial_number = fields.Char('Serial number', required=True, index=True, copy=False, default='New')
    vehicle_type = fields.Selection([("Car", "Car"), ("Bus","Bus"), ("MiniBus","MiniBus"), ("MicroBus","MicroBus")])
    certificate_types = fields.Many2one(comodel_name="iti.certificate.type")
    traffic_department = fields.Many2one(comodel_name="iti.certificate.trafficdepartment")
    customer = fields.Many2many("res.partner", "related_certificate_id")
    car_brand = fields.Many2one(comodel_name="iti.certificate.carbrand")
    price = fields.Integer()
    motor_number = fields.Integer()
    chassis_number = fields.Char()
    allow_print = fields.Boolean()
    log_history_ids = fields.One2many("iti.certificate.certificates.log", "certificate_id")
    current_date = fields.Text()


    # @api.multi
    @api.model
    def create(self, vals):
        certificate = super().create(vals)
        print(certificate.allow_print)
        certificate.allow_print = True
        print(certificate.allow_print)
        return certificate

    # @api.model_create_multi
    def print_report(self):
        # print(self.allow_print)
        if self.env.user.has_group("certificates.iti_super_user_certificates_group"):
            return self.env.ref('certificates.certificate_report').report_action(self)
        else:
            if self.allow_print:
                self.allow_print = False
                date_today = str(date.today())
                self.current_date = date_today
                self.env['iti.certificate.certificates.log'].create({
                    "description": f'Printed on {date_today}',
                    "certificate_id": self.id
                })
                return self.env.ref('certificates.certificate_report').report_action(self)
            else:
                raise exceptions.UserError('You are not allowed to print the certificate for multiple times')

    def allow_reprint(self):
        self.allow_print = True

    class LogHistory(models.Model):
        _name = "iti.certificate.certificates.log"

        description = fields.Char()
        certificate_id = fields.Many2one("iti.certificate.certificates")
    # # @api.model
    # # @api.Environment
    # @api.model_create_multi
    # def print_report(self, cr, uid, ids, context=None):
    #     if context is None:
    #         context = {}
    #     data = {}
    #     data['ids'] = context.get('active_ids', [])
    #     data['model'] = context.get('active_model', 'ir.ui.menu')
    #     return self.pool['report'].get_action(cr, uid, [], 'certificates.certificate_report', data=data, context=context)
    # @api.model
    # def create(self, vals):
    #     print(self.env['ir.sequence'].next_by_code.dict)
    #     vals['serial_number'] = self.env['ir.sequence'].next_by_code['iti.certificate.certificates']
    #     return super(Certificates, self).create(vals)

    # def _car_model_field_get(self, context=None):
    #     # mf = self.pool.get('ir.model.fields')
    #     today_date = date.today()
    #     years = list(range(today_date.year, today_date.year-20))
    #     return years
    # # _columns = {
    # # "car_model" : fields.Selection(_car_model_field_get, "Product Field", size=32, required=True),
    # # }
    # car_model = fields.Selection(_car_model_field_get, "Product Field", size=32, required=True)
