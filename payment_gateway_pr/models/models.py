# -*- coding: utf-8 -*-
from odoo import models, fields, api


class payment_gateway_pr(models.Model):
     _name = 'payment_gateway_pr.payment_gateway_pr'
     _description = 'payment_gateway_pr.payment_gateway_pr'

     name = fields.Char()
     package = fields.Char()
    
     price = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

    # @api.depends('value')
     #def _value_pc(self):
      #   for record in self:
       #      record.value2 = float(record.value) / 100
