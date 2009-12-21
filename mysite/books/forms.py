import datetime

from django import forms

from mysite.books.widgets import DateTimeWidget


class EditorForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=40, required=False)
    birth_day = forms.DateField(widget=DateTimeWidget, required=False)
    bio = forms.CharField(max_length=200,
                          widget=forms.Textarea, required=False)
    contacts = forms.CharField(max_length=50, required=False)
