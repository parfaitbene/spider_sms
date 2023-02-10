# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SpiderSmsList(models.Model):
    _name = 'spider_sms.list'
    _description = 'Spider SMS partners list'

    name = fields.Char('name')
    description = fields.Html('description')
    partner_ids = fields.Many2many('res.partner', string='Partner(s)')
    