from django import forms


class EditorForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=40, required=False)
    bio = forms.CharField(max_length=200,
                          widget=forms.Textarea, required=False)
    contacts = forms.CharField(max_length=50, required=False)
