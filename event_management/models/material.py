from odoo import api, fields, models


class Material(models.Model):
    _name = 'event_management.material'
    _description = 'Event Materials'

    type = fields.Selection([('sound equipment', 'Sound Equipment'), ('projection equipment', 'Projection Equipment')],
                            string='Equipment type')
    tools = fields.Char(string='Tools', required=True)
    event_id = fields.Many2one(comodel_name='event.event', string='Event')

