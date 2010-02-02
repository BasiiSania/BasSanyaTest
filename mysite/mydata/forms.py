import datetime

from django import forms
from django.db import models

from mysite.mydata.widgets import DateTimeWidget
from mysite.mydata.models import Author


class EditorForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs = {
                                       'cols': '15',
                                       'rows': '5'}),
                                             required = False)
    birth_day = forms.DateField(widget=DateTimeWidget, required=False)
	
    class Media:
        extend = False
        css = {'all': ("calendar/calendar-win2k-cold-1.css",)}
        js = ("calendar/calendar.js",
              "calendar/lang/calendar-en.js",
              "calendar/calendar-setup.js")

    class Meta:
        model = Author
        fields = ['contacts', 'bio', 'birth_day', 'last_name', 'first_name']
