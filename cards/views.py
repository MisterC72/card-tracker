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

# import the CardForm
from .forms import CardForm


# Create a new view called CardListView
class CardListView(ListView):
    model = Card
    template_name = "cards/card_list.html"
    context_object_name = "cards"
    # order the cards by the highest balance
    ordering = ["-balance"]

    # get total balance of all cards
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # filter the queryset to only include active cards
        context["cards"] = Card.objects.filter(is_active=True)
        context["total_balance"] = sum([card.balance for card in context["cards"]])
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
