# create url patterns for the cards app

from django.urls import path

from .views import CardListView, CardCreateView, CardDetailView

urlpatterns = [
    path("", CardListView.as_view(), name="card_list"),
    path("new/", CardCreateView.as_view(), name="card_create"),
    path("<int:pk>/", CardDetailView.as_view(), name="card_detail"),
]
