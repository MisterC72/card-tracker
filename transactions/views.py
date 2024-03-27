from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy
from .models import Transaction
from cards.models import Card

from .forms import TransactionForm

# import the Card model
from cards.models import Card


# transaction CreateView
class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/transaction_create.html"

    def get_initial(self):
        initial = super().get_initial()
        # Assuming the URLconf captures "card_id" as the card's ID
        card_id = self.kwargs.get("card_id")
        if card_id:
            initial["card"] = get_object_or_404(Card, pk=card_id)
        return initial

    def form_valid(self, form):
        # Set the card directly on the form instance before saving
        card_id = self.kwargs.get("card_id")
        form.instance.card = get_object_or_404(Card, pk=card_id)

        # Logic to update the card's balance based on the transaction type
        card = form.instance.card
        amount = form.cleaned_data["amount"]
        transaction_type = form.cleaned_data["type"]
        if transaction_type == "charge":
            card.balance += amount  # Assuming "charge" means adding amount
        else:
            card.balance -= amount
        card.save()
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the card's detail view after creating a transaction
        card_id = self.kwargs.get("card_id")
        return reverse_lazy("card_detail", kwargs={"pk": card_id})


# transaction ListView
class TransactionListView(ListView):
    model = Transaction
    template_name = "transactions/transaction_list.html"
    context_object_name = "transactions"
    ordering = ["-date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transactions"] = Transaction.objects.all()
        context["total_payments"] = sum(
            [
                transaction.amount
                for transaction in context["transactions"]
                if transaction.type == "payment"
            ]
        )
        context["total_charges"] = sum(
            [
                transaction.amount
                for transaction in context["transactions"]
                if transaction.type == "charge"
            ]
        )
        context["total_transactions"] = sum(
            [transaction.amount for transaction in context["transactions"]]
        )
        return context
