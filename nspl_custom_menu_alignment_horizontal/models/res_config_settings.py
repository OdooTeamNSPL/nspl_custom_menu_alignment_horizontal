# -*- coding: utf-8 -*-
# This file is part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    menu_layout_horizontal = fields.Selection(
        selection=[
            ('default', 'Default'),
            ('horizontal', 'Horizontal'),
        ],
        string="Menu Layout",
        related='company_id.menu_layout_horizontal',
        readonly=False,
    )


class ResCompany(models.Model):
    _inherit = 'res.company'

    menu_layout_horizontal = fields.Selection(
        selection=[
            ('default', 'Default'),
            ('horizontal', 'Horizontal'),
        ],
        string="Menu Layout",
        default='default',
    )
