from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=40, verbose_name='Second name')
    birth_day = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    bio = models.CharField(max_length=200, verbose_name='Bio')
    contacts = models.CharField(max_length=50, verbose_name='Contacts')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class AuthRequest(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)