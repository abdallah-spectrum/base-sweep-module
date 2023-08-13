from odoo import models, fields

class BaseSweepModule(models.Model):
    _name = 'base.sweep.module'
    _description = 'Base Sweep Module'

    name = fields.Char(string='Name', required=True)

