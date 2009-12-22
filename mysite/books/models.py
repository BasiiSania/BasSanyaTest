from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    birth_day = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True)
    contacts = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class AuthRequest(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)