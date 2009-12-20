"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from mysite.books.models import Author
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    fixtures = ['initial_data.json']

    def test_auth_correct(self):
        data = Author.objects.get(pk=1)
        data2 = User.objects.get(pk=2)
        self.assertEquals(data.first_name, 'Oleksandr')
        self.assertEquals(data.last_name, 'Basiy')
        self.assertEquals(data.contacts, '5156696, Kyiv')
        self.assertEquals(data2.username, 'Sasha')
