from django.shortcuts import render

# import views from django
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# import reverse from django.urls
from django.urls import reverse

# import the Card model
from .models import Card


# Create a new view called CardListView
class CardListView(ListView):
    model = Card
    template_name = "cards/card_list.html"
    context_object_name = "cards"
    # order the cards by the highest balance
    ordering = ["-balance"]


# Create a new view called CardCreateView
class CardCreateView(CreateView):
    model = Card
    template_name = "cards/card_create.html"
    fields = ["provider", "limit", "balance", "is_zero_percent", "zero_percent_end"]

    # redirect to the card list view after creating a new card
    def get_success_url(self):
        return reverse("card_list")


# Create a new view called CardDetailView
class CardDetailView(DetailView):
    model = Card
    template_name = "cards/card_detail.html"
    context_object_name = "card"
