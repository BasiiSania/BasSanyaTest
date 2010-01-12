import datetime

from django.core.cache import cache


def log_models_change(**kwargs):
    if kwargs['sender'].__name__ != 'LogDB':
        from mysite.books.models import LogDB
#    if action in kwargs.keys():
#        content.append(kwargs['action'] + " in ")

        if kwargs['created']:
            to_descr = "created"
        else:
            to_descr = "changes"
        to_log_db = LogDB(moment = datetime.datetime.now(), 
                     description =  "%s in %s" %(to_descr, kwargs['sender'].__name__))
        to_log_db.save()


def log_models_delete(**kwargs):
    if kwargs['sender'].__name__ != 'LogDB':
        from mysite.books.models import LogDB
        to_log_db = LogDB(moment = datetime.datetime.now(), 
                     description =  "deletes in %s" %kwargs['sender'].__name__)
        to_log_db.save()