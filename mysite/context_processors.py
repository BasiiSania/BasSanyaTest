# -*- coding: utf-8 -*-
from django.conf import settings


def django_settings(request):
    "A context processor that provides django settings"
    s_dict = {}
    for atr in settings.get_all_members():
        if ('A'<atr[0]) and (atr[0]<'Z'):
            s_dict[atr] = settings.__getattr__(atr)
    return s_dict
