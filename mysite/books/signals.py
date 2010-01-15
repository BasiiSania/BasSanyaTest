from datetime import datetime

from django.core.cache import cache


def log_models_change(sender, **kwargs):
    if sender.__name__ != 'LogDB':
        from_post_delete = True
        for k in kwargs:
            if k == "created":
                from_post_delete = False
                from mysite.books.models import LogDB
                if kwargs['created']:
                    to_descr = "created"
                else:
                    to_descr = "changes"
                to_log_db = LogDB(moment = datetime.now(), 
                             description =  "%s in %s" %(to_descr, sender.__name__))
                to_log_db.save()
        if from_post_delete:
            from mysite.books.models import LogDB
            to_log_db = LogDB(moment = datetime.now(), 
                         description =  "deletes in %s" %sender.__name__)
            to_log_db.save()