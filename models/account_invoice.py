from openerp import models, fields, api

class provem_ro_account_invoice(models.Model):

    _inherit = 'account.invoice'

    notes = fields.Text('Observaciones')

    @api.one
    @api.depends('invoice_line_ids.discount')
    def _compute_total_discount(self):
        self.total_discount = sum(line.amount_discount for line in self.invoice_line_ids)


    total_discount = fields.Float('Descuento total', compute='_compute_total_discount')

class provem_ro_account_invoice_line(models.Model):

    _inherit = 'account.invoice.line'

    @api.one
    @api.depends('price_unit', 'discount', 'quantity')
    def _compute_amount_discount(self):
        descuneto = self.price_unit * ((self.discount or 0.0) / 100.0)
        self.amount_discount = descuneto * self.quantity

    amount_discount = fields.Float(compute='_compute_amount_discount')




