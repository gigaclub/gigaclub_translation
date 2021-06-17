from odoo import fields, models, api


class GCUser(models.Model):
    _inherit = 'gc.user'

    language_id = fields.Many2one(comodel_name="gc.language", default=lambda x: x.env["gc.language"].search([("default","=",True)]))
