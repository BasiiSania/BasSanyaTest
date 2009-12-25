import datetime

from django.core.cache import cache
from django.core.files import File


def log_models_change(**kwargs):
    f = open(
        'C:/Documents and Settings/Ingusik/BasSanyaTest/mysite/media/log.txt',
        'a')
    log = File(f)
    content = '\ntime: %s' \
              %datetime.datetime.now().strftime("%Y %b %d %H:%M:%S")
#    if action in kwargs.keys():
#        content.append(kwargs['action'] + " in ")
    if kwargs['created']:
        content = "%s; created in %s \n" %(content, kwargs['sender'].__name__)
    else:
        content = "%s; changes in %s \n" %(content, kwargs['sender'].__name__)
    log.write(content)
    log.close()


def log_models_delete(**kwargs):
    print kwargs
    f = open(
        'C:/Documents and Settings/Ingusik/BasSanyaTest/mysite/media/log.txt',
        'a')
    log = File(f)
    content = 'time: ' + datetime.datetime.now().strftime("%Y %b %d %H:%M:%S")
    content = "%s; deletes in %s \n" %(content, kwargs['sender'].__name__)
    log.write(content)
    log.close()
