# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse
from ussd.core import UssdView, UssdRequest


class CustomUssdView(UssdView):

    @staticmethod
    def post(req):
        list_of_inputs = req.data['text'].split("*")
        text = "*" if len(list_of_inputs) >= 2 and list_of_inputs[-1] == "" and list_of_inputs[-2] == "" else \
            list_of_inputs[-1]

        session_id = req.data['sessionId']
        if req.data.get('use_built_in_session_management', False):
            session_id = None
        ussd_request = UssdRequest(
            phone_number=req.data['phoneNumber'].strip('+'),
            session_id=session_id,
            ussd_input=text,
            service_code=req.data['serviceCode'],
            language=req.data.get('language', 'en'),
            use_built_in_session_management=req.data.get(
                'use_built_in_session_management', False)
        )

        return ussd_request

    @staticmethod
    def get_customer_journey_namespace(req):
        screen_namespace = "BFS_namespace"
        service_code = dict(req.data)['serviceCode'][0]
        if service_code == '*384*99900#':
            screen_namespace = "BFS_namespace2"
        return screen_namespace

    @staticmethod
    def get_customer_journey_conf(req):
        screen = "./UssdApp/static/screens.yml"
        service_code = dict(req.data)['serviceCode'][0]
        if service_code == '*384*99900#':
            screen = "./UssdApp/static/screens2.yml"
        return screen

    def ussd_response_handler(self, ussd_response):
        if ussd_response.status:
            res = 'CON' + ' ' + str(ussd_response)
            response = HttpResponse(res)
        else:
            res = 'END' + ' ' + str(ussd_response)
            response = HttpResponse(res)
        return response


# Project Landing Page
def index(request):
    return HttpResponse("<b>Welcome to USSD App Page!</b>")


