from odoo import api, fields, models


class EventInherit(models.Model):
    _inherit = 'event.event'

    theme_event = fields.Char(string='Theme Event')
    event_organizer_id = fields.Many2one('event_management.organizer', string='Organizer')
    customer_id = fields.Many2one('res.partner', string='Customer')
    material_ids = fields.One2many('event_management.material', 'event_id', string='Materials')
