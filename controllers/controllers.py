# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo.http import request
import simplejson

logger = logging.getLogger(__name__)

class VitApplicant(http.Controller):
    @http.route('/vit/ap', type='http', auth='public', website=True)
    def index(self, **kw):
        applicants = request.env['hr.applicant'].search([])
        return request.render("vit_applicant.index",{
            "applicants" : applicants
        })
# class VitApplicant(http.Controller):
#     @http.route('/vit_applicant/vit_applicant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_applicant/vit_applicant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_applicant.listing', {
#             'root': '/vit_applicant/vit_applicant',
#             'objects': http.request.env['vit_applicant.vit_applicant'].search([]),
#         })

#     @http.route('/vit_applicant/vit_applicant/objects/<model("vit_applicant.vit_applicant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_applicant.object', {
#             'object': obj
#         })