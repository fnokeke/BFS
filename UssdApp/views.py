# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from ussd.core import UssdView, UssdRequest
from UssdApp.models import UssdLog
from UssdApp import error_terms


class CustomUssdView(UssdView):

    @staticmethod
    def post(req):
        print('req.data = ', req.data)
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
        if service_code == '*384*888#':
            screen_namespace = "BFS_namespace2"
        elif service_code == '*384*11100#':
            screen_namespace = "BFS_testing"
        return screen_namespace

    @staticmethod
    def get_customer_journey_conf(req):
        screen = "./UssdApp/static/hospital_multi_lang.yml"
        service_code = dict(req.data)['serviceCode'][0]
        if service_code == '*384*888#':
            screen = "./UssdApp/static/chv_multi_lang.yml"
        elif service_code == '*384*11100#':
            screen = "./UssdApp/static/hospital_multi_lang.yml"
        return screen

    def ussd_response_handler(self, ussd_response):
        self.log_response(ussd_response)

        if ussd_response.status:
            res = 'CON' + ' ' + str(ussd_response)
            response = HttpResponse(res)
        else:
            res = 'END' + ' ' + str(ussd_response)
            response = HttpResponse(res)
        return response

    def log_response(self, ussd_response):
        sess = ussd_response.session._session
        interaction = sess['ussd_interaction']
        screen_answered, has_error, seconds_spent = None, False, 0

        if len(interaction) == 1:
            print('********first ussd call made*****************')
            screen_answered = 'ussd_initiated'

        elif len(interaction) > 1:
            screen_answered = interaction[-2]['screen_name']
            print('**********last_answered_screen******** = ', screen_answered)
            print('**********last_input_entered******** = ', sess['input'])

            has_error = False
            for phrase in error_terms.LIST_OF_ERROR_PHRASES:
                if phrase in interaction[-1]['screen_text']:
                    has_error = True
                    break

            if has_error:
                print("(((((((((((((((Error in user entry!)))))))))))))))))")

            seconds_spent = interaction[-2]['duration'] / 1000
            print('**********time_spent******** = ', seconds_spent, "seconds")

        # next_screen = interaction[-1]['screen_name']
        next_screen = sess['_ussd_state']['next_screen']
        print('---------------------------------------------------------------------------')
        print('**********next_screen******** = ', next_screen)
        print('**********next_text******** = \n', interaction[-1]['screen_text'])
        print()
        print()

        UssdLog.add({
            'phone_number': sess['phone_number'],
            'session_id': sess['session_id'],
            'service_code': sess['service_code'],
            'language': sess.get('language', 'en'),
            'screen_answered': screen_answered,
            'ussd_input': sess['input'],
            'has_error': has_error,
            'seconds_spent': seconds_spent,
            'next_screen': next_screen
        })


# class QualityCheck:
#     @staticmethod
#     def check_broken_link(requests, data):
#         try:
#             url = requests.head(data)
#             if url.status_code == 200 or url.status_code == 302 or url.status_code == 301:
#                 return True
#         except requests.exceptions.SSLError as e:
#             print("(((((((((((((((SSL Error)))))))))))))))))")
#             print(e)
#             return False


# Project Landing Page
def index(request):
    return HttpResponse("<b>Welcome to USSD App Page!</b>")
