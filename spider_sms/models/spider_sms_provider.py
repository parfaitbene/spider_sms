# -*- coding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import UserError

class SpiderSmsProvider(models.Model):
    _name = 'spider_sms.provider'
    _description = 'spider_sms.provider'
    
    name = fields.Char('Name')
    code = fields.Char('Code')
    sender_name = fields.Char('Sender Name')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Active')
    ], string='State')

    def send_sms(self):
        raise UserError(_('SMS provider not found. Please create and activate one to continue'))
    