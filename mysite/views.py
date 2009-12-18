# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime
from django.core import management
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from books.models import Author


def hello(request):
    return HttpResponse("Hello, world!")


def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)
#
#    now = datetime.datetime.now()
#    return render_to_response('current_datetime.html', {'current_date': now})
#
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())


@login_required
def main_page(request):
    data = Author.objects.get(first_name = 'Oleksandr')
    html = "<html><body><p> About me.</p>"
    html = html + "<p>First name: %s</p>" % data.first_name
    html = html + "<p>Last name: %s</p>" % data.last_name
    html = html + "<p>Bio: %s</p>" % data.bio
    html = html + "<p>Contacts: %s</p>" % data.contacts
    html = html + "</body></html>"
    return HttpResponse(html)
