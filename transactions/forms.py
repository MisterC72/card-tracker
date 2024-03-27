from django import forms
from django.forms.widgets import DateInput
from .models import Transaction


# TransactionForm
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount", "date", "type", "notes"]
        widgets = {
            "date": DateInput(attrs={"type": "date"}, format="%d/%m/%Y"),
            "type": forms.RadioSelect,
        }
