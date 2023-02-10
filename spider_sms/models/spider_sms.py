# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api

class SpiderSms(models.Model):
    _name = 'spider_sms.sms'
    _description = 'spider_sms.sms'

    name = fields.Char(default=lambda self: self._get_name())
    message = fields.Text()
    state = fields.Selection([('draft', 'Draft'), ('done', 'Sent')], string='State')
    provider_id = fields.Many2one('spider_sms.provider', string='Provider')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    list_ids = fields.Many2many('spider_sms.list', string='Contact lists')
    partner_ids = fields.Many2many('res.partner', string='Contacts')

    def _get_name(self):
        self.name = fields.Datetime.to_string(datetime.now())

    def send(self):
        "Send SMS  with right provider"
        return
