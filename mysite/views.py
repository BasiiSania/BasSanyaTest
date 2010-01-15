# -*- coding: utf-8 -*-
import datetime

from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from books.models import Author


def hello(request):
    return HttpResponse("Hello, world! I am alive!")


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())


@login_required
def main_page(request):
    data = Author.objects.get(pk=1)
    return render_to_response('about_author.html', {
        'data': data, },
        context_instance = RequestContext(request))
