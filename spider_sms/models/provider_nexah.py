# -*- coding: utf-8 -*-

import requests

from odoo import api, fields, models, _

class ProviderNexah(models.Model):
    _inherit = 'spider_sms.provider'
    
    user = fields.Char('User')
    password = fields.Char('Password')
    send_sms_url = fields.Char('Send SMs Url')
    get_balance_url = fields.Char('Get BAlance Url')
    get_dr_notification_url = fields.Char('Get DR NOtification Url')


    def nexah_send_sms(self):
        """Nexah provider method to send sms with right parameters"""
        return

    