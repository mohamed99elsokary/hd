from django import forms
from . import models


class NameForm(forms.ModelForm):

    your_name = forms.CharField(label="Your name", max_length=100)
    subject = forms.CharField(max_length=100)

    class Meta:
        model = models.Products

        fields = "__all__"
