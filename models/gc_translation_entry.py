from odoo import fields, models


class GCTranslationEntry(models.Model):
    _name = 'gc.translation.entry'

    content = fields.Text(required=True)
    translation_id = fields.Many2one(comodel_name="gc.translation")
    translation_ids = fields.Many2many(comodel_name="gc.translation")
    language_id = fields.Many2one(comodel_name="gc.language")
