from odoo import models, fields


class GCTranslation(models.Model):
    _name = "gc.translation"

    name = fields.Char(required=True)
    var_count = fields.Integer()
    translation_entry_ids = fields.One2many(comodel_name="gc.translation.entry", inverse_name="translation_id")

    _sql_constraints = [
        ('name_unique', 'unique (name)', 'name must be unique!')
    ]
