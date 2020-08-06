from django import forms
from .models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Краткое описание')
    description = forms.CharField(required=False, label='Полное описание', widget=forms.Textarea)
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
