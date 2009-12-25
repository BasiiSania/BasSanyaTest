from django.db import models
from django.db.models import signals
from django.dispatch import dispatcher
from mysite.books.signals import log_models_change
from mysite.books.signals import log_models_delete


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

signals.post_save.connect(log_models_change, sender=None)
signals.post_delete.connect(log_models_delete, sender=None)
#dispatcher.connect(log_models_change,signal=signals.post_init,sender=None)
#dispatcher.connect(log_models_change,signal=signals.post_save,sender=None)
#dispatcher.connect(log_models_change,signal=signals.post_delete,sender=None)
