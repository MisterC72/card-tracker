# create url patterns for the cards app

from django.urls import path

from .views import CardListView, CardCreateView, CardDetailView, CardUpdateView

urlpatterns = [
    path("", CardListView.as_view(), name="card_list"),
    path("new/", CardCreateView.as_view(), name="card_create"),
    path("<int:pk>/", CardDetailView.as_view(), name="card_detail"),
    path("<int:pk>/update/", CardUpdateView.as_view(), name="card_update"),
]
