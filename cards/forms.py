from django import forms
from django.forms.widgets import DateInput
from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            "provider",
            "limit",
            "balance",
            "is_zero_percent",
            "zero_percent_end",
            "is_active",
        ]
        widgets = {
            "zero_percent_end": DateInput(attrs={"type": "date"}, format="%d/%m/%Y"),
        }
