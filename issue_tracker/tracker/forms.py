from django import forms
from .models import Issue, Type, Status, Project

class IssueForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())

    class Meta:
        model = Issue
        fields = ["title", "description", "type", "status"]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('id',)