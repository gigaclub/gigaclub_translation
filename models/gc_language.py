from odoo import fields, models


class GCLanguage(models.Model):
    _name = 'gc.language'

    name = fields.Char(required=True)
    entry_ids = fields.One2many(comodel_name="gc.translation.entry", inverse_name="translation_id")
