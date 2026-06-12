# ©  2008-2023 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


from odoo import fields, models, tools


class AccountStatementReport(models.Model):
    _name = "account.statement.report"
    _description = "Account Statement Report"
    _auto = False
    _order = "date desc"

    date = fields.Date("Date", readonly=True)
    journal_id = fields.Many2one("account.journal", "Journal", readonly=True)
    journal_type = fields.Selection(
        [
            ("sale", "Sales"),
            ("purchase", "Purchase"),
            ("cash", "Cash"),
            ("bank", "Bank"),
            ("general", "Miscellaneous"),
        ],
        readonly=True,
    )
    statement_id = fields.Many2one("account.bank.statement", "Statement", readonly=True)
    state = fields.Selection(
        selection=[
            ("open", "New"),
            ("posted", "Processing"),
            ("confirm", "Validated"),
        ],
        string="Status",
        readonly=True,
    )
    partner_id = fields.Many2one("res.partner", "Partner", readonly=True)
    balance_start = fields.Monetary("Starting Balance", readonly=True)
    balance_end_real = fields.Monetary("Ending Balance", readonly=True)

    amount = fields.Monetary(currency_field="currency_id")
    currency_id = fields.Many2one("res.currency", "Currency", readonly=True)

    # selecteaza datele din account.bank.statement.line si account.bank.statement
    def _select(self):
        return """
            SELECT
                s.journal_id, s.state, s.balance_start, s.balance_end_real,
                l.id as id, m.date,  l.statement_id, l.partner_id, l.amount, l.currency_id,
                j.type as journal_type
            FROM account_bank_statement_line l
            LEFt join account_move m ON (m.id = l.move_id)
            LEFT JOIN account_bank_statement s ON (s.id = l.statement_id)
            LEFT JOIN account_journal j ON (j.id = s.journal_id)
        """

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE OR REPLACE VIEW {} AS ({})""".format(self._table, self._select()))
