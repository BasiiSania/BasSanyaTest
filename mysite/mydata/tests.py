# -*- coding: utf-8 -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import TestCase
from django.contrib.auth.models import User

from mysite.mydata.models import Author


class FixturesTest(TestCase):
    fixtures = ['initial_data.json']

    def test_auth_correct(self):
        data = Author.objects.get(pk=1)
        data2 = User.objects.get(pk=2)
        self.assertEquals(data.first_name, 'Oleksandr')
        self.assertEquals(data.last_name, 'Basiy')
        self.assertEquals(data.contacts, '5156696, Kyiv')
        self.assertEquals(data2.username, 'Sashok')

__test__ = {"all_doctest": """
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('iamtest2', 'iambot@example.com', 'password')
>>> user.save()
>>> from django.test.client import Client
>>> c = Client()
>>> response = c.get('/')
>>> response.status_code
302
>>> c.login(username = 'iamtest2',password = 'password')
True
>>> response = c.get('/')
>>> response.status_code
200
>>> print response.context['user'].username
iamtest2
>>> response = c.get('/accounts/login/?next=/')
>>> response.status_code
200
>>> response = c.post('/accounts/login/?next=/',\
               {'username':'testuser','password':'testpassword'})
>>> response.status_code
200
>>> from mysite.mydata.models import AuthRequest
>>> a = AuthRequest.objects.get(enter_login = "testuser")
>>> a.enter_pass == "testpassword"
True
>>> a.delete()
>>> #response = c.post('/accounts/login/?next=/',{'username':'','pass':''})
... from middleware import SaveAuthenticationRequestMiddleware
>>> o = SaveAuthenticationRequestMiddleware()
>>> class MyRequest(object):
...     method = 'POST'
...     path = '/accounts/login/'
...     POST = {}
>>> request = MyRequest()
>>> o.process_request(request)#end
>>> response = c.post('/accounts/login/?next=/',{'username':'','password':''})
>>> response.status_code
200
>>> response = c.get('/editor/')
>>> response.status_code
200
>>> response.template.name
'editor_form.html'
>>> from django.conf import settings
>>> settings.TIME_ZONE == response.context['TIME_ZONE']
True
>>> response = c.post('/editor/')
>>> response.status_code
302
>>> response = c.post('/editor/', {'last_name':'eman_tsal'})
>>> response.status_code
302
>>> from mysite.mydata.models import Author
>>> a = Author.objects.get(pk=1)
>>> a.last_name
u'eman_tsal'
"""}
