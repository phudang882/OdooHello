from odoo import models, fields, api
from odoo.exceptions import AccessError
import threading
class Document(models.Model):
    _name = 'document.manager'
    _description = 'Document Manager'
    title = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    link = fields.Char(string="Link")
    note = fields.Text(string="Note")
    time = fields.Date(string="Creat time",default= fields.Date.today())
    group_id = fields.Many2one(comodel_name="res.groups",string="Group")
    owner = fields.Many2one(comodel_name="res.users",string="Owner",default=lambda self: self.env.user)
    state = fields.Selection(selection=[("accept","Accept"),("apply","Apply"),("reject","Reject")],string="State",required=True)
    