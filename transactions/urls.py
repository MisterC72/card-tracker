from django.urls import path
from .views import TransactionListView, TransactionCreateView

urlpatterns = [
    path("", TransactionListView.as_view(), name="transaction_list"),
    path(
        "cards/<int:card_id>/add_transaction/",
        TransactionCreateView.as_view(),
        name="add_transaction",
    ),
]
