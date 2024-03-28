from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from .models import Card
from .forms import CardForm


# Create a new view called CardListView
class CardListView(ListView):
    model = Card
    template_name = "cards/card_list.html"
    context_object_name = "cards"
    ordering = ["-balance"]

    def get_queryset(self):
        # Filter the queryset to only include active cards and order by balance
        queryset = (
            super().get_queryset().filter(is_active=True).order_by(self.ordering[0])
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Now, since context['cards'] is already ordered and filtered, we calculate the total balance
        # Using aggregate(Sum()) to calculate total balance efficiently
        context["total_balance"] = Card.objects.filter(is_active=True).aggregate(
            total=Sum("balance")
        )["total"]
        return context


# Create a new view called CardCreateView
class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    template_name = "cards/card_create.html"

    # redirect to the card list view after creating a new card
    def get_success_url(self):
        return reverse("card_list")


# Create a new view called CardDetailView
class CardDetailView(DetailView):
    model = Card
    template_name = "cards/card_detail.html"
    context_object_name = "card"


# Create a new view called CardUpdateView
class CardUpdateView(UpdateView):
    model = Card
    form_class = CardForm
    template_name = "cards/card_update.html"

    # redirect to the card detail view after updating a card
    def get_success_url(self):
        return reverse("card_detail", kwargs={"pk": self.object.pk})
