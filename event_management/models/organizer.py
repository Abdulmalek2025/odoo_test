import re
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Organizer(models.Model):
    _name = 'event_management.organizer'
    _description = 'Event Organizer'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    phone = fields.Integer(string='Phone')
    mail = fields.Char(string='Email')
    organizer_type = fields.Selection([('mr.', 'Mr.'), ('mrs.', 'Mrs.')])

    @api.constrains('mail')
    def _check_valid_mail(self):
        for rec in self:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", rec.mail):
                raise ValidationError(_("{} is Invalid email".format(rec.mail)))

    def name_get(self):
        return [(rec.id, "%s %s" % (rec.first_name, rec.last_name)) for rec in self]