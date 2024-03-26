from django.shortcuts import render

# import views from django
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# import the Card model
from .models import Card


# Create a new view called CardListView
class CardListView(ListView):
    model = Card
    template_name = "cards/card_list.html"
    context_object_name = "cards"


# Create your views here.
