from django import forms
from .models import Type, Status

class IssueForm(forms.Form):
    title = forms.CharField(label='title', max_length=70)
    description = forms.TextInput(attrs={"class": "special"})
    _type = forms.ModelChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())