from odoo import _, models
from odoo.exceptions import AccessError


class AccountMove(models.Model):
    _inherit = "account.move"

    def js_assign_outstanding_line(self, line_id):
        if not self.env.user.has_group(
            "arga_assign_outstanding_access.group_assign_outstanding"
        ):
            raise AccessError(_(
                "You are not allowed to assign outstanding payments or credits. "
                "Ask your administrator to grant the Assign Outstanding access."
            ))
        return super().js_assign_outstanding_line(line_id)
