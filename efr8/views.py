# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from constants import ports_list, vessels_list, container_size_list, container_type_list, delivery_type_list, transporter_list, icd_cfs_list, LINER_MANIFEST_FILE_NAME
from utils import write_to_file, read_from_file

# Create your views here.
def home(request):
    return render(request, 'efr8/home.html')


def liner(request):
    return render(request, 'efr8/liner.html')


@csrf_exempt
def liner_create_manifest(request):
    if request.method == 'GET':
        return render_to_response('efr8/liner_create_manifest.html', {
        'ports_list': ports_list,
        'vessels_list': vessels_list,
        'container_size_list': container_size_list,
        'container_type_list': container_type_list,
        'delivery_type_list': delivery_type_list,
        'transporter_list': transporter_list,
        'icd_cfs_list': icd_cfs_list,
        })
    else:
        data = [request.POST]
        write_to_file(data, LINER_MANIFEST_FILE_NAME)
        return HttpResponse(json.dumps({'success': True}))


def transporter(request):
    return render(request, 'efr8/transporter.html')


def liner_view_manifests(request):
    data = read_from_file(LINER_MANIFEST_FILE_NAME)
    return render_to_response('efr8/liner_view_manifests.html', {
        'manifest_list': data
    })


def port(request):
    return render(request, 'efr8/port.html')
