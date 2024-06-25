##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models

class ProductCategory(models.Model):
    _name = 'product.category'
    _inherit = ['product.category', 'mail.thread', 'mail.activity.mixin']
