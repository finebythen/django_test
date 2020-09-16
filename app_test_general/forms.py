from django.forms import ModelForm
from django import forms
from .models import *


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = [
            'customer',
            'project',
            'cluster',
            'user_created',
            'date_created',
        ]


class ExampleForm(ModelForm):
    class Meta:
        model = WidgetTweaksExamples
        exclude = [
            'date_str',
        ]


class TransportExampleForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '...'}))
    gender = forms.ChoiceField(choices=genders, widget=forms.RadioSelect)

    class Meta:
        model = TransportExamples
        exclude = []
