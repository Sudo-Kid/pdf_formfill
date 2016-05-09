from django import forms

from . import models


class ApplForm(forms.ModelForm):
    class Meta:
        model = models.Appl
        exclude = ['id']
