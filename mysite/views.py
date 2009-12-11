# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime
from books.models import Author
from django.core import management

def hello(request):
    return HttpResponse("Здравствуй, Мир!")
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def main_page(request):
    management.call_command('loaddata', 'initial_data.json', verbosity=0)
    data = Author.objects.get(first_name = 'Oleksandr')
    html = "<html><body><p> About me.</p>"
    html = html + "<p>First name: %s</p>" % data.first_name
    html = html + "<p>Last name: %s</p>" % data.last_name
    html = html + "<p>Bio: %s</p>" % data.bio
    html = html + "<p>Contacts: %s</p>" % data.contacts
#    for i,k in data
#        html1 = "<p>%s: %s</p>" % i,k
#        html = html + html1
    html = html + "</body></html>"
    return HttpResponse(html)