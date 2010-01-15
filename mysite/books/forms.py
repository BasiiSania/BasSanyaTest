import datetime

from django import forms
from django.db import models

from mysite.books.widgets import DateTimeWidget
from mysite.books.models import Author


class EditorForm(forms.ModelForm):
    birth_day = forms.DateField(widget=DateTimeWidget, required=False)

    class Meta:
        model = Author
        fields = ['contacts', 'bio', 'birth_day', 'last_name', 'first_name']
