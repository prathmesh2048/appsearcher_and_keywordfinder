from django import forms
from . models import Url


class DataForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('url',)
