# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'efr8/home.html')


def liner(request):
    return render(request, 'efr8/liner.html')


def transporter(request):
    return render(request, 'efr8/transporter.html')


def port(request):
    return render(request, 'efr8/port.html')
