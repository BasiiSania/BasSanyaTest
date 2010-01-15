# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.dispatch import dispatcher

from mysite.books.signals import log_models_change


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    birth_day = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True)
    contacts = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class AuthRequest(models.Model):
    enter_login = models.CharField(max_length=30)
    enter_pass = models.CharField(max_length=40)

    def __unicode__(self):
        return '%s, %s' % (self.enter_login, self.enter_pass)


class LogDB(models.Model):
    moment = models.DateTimeField()
    description = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s: %s' % (self.moment.strftime("%Y %b %d, %H:%M:%S"), self.description)


signals.post_save.connect(log_models_change, sender=None)
signals.post_delete.connect(log_models_change, sender=None)


"""
>>> from django.contrib.auth.models import User
>>> User.objects.get(pk=2)
<User: Sashok>
>>> from mysite.books.models import Author
>>> Author.objects.get(pk=1)
<Author: Oleksandr Basiy>
>>> a = Author(first_name = "ABCDEF")
>>> a.save()
>>> a = Author.objects.get(first_name = "ABCDEF")
>>> print a.first_name.encode('utf-8')
ABCDEF
>>> from mysite.books.models import AuthRequest
>>> a = AuthRequest(enter_login = "ABCDEF")
>>> a.save()
>>> a = AuthRequest.objects.get(enter_login = "ABCDEF")
>>> print a.enter_login.encode('utf-8')
ABCDEF
>>> from mysite.books.models import LogDB
>>> from datetime import datetime
>>> a = LogDB(moment = datetime.now(), description =  "testAPGOFDFLDPS")
>>> a.save()
>>> m = a.moment
>>> a = LogDB.objects.get(moment = m)
>>> print a.description.encode('utf-8')
testAPGOFDFLDPS
"""