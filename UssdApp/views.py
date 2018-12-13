# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    return HttpResponse("<b>True Ussd App - Welcome Page!</b>")


def helloworld(request):
    return HttpResponse("<b>Hello World to everyone out there!</b>")


def maxy(request):
    return HttpResponse("<b>Hello Maxy!</b>")
