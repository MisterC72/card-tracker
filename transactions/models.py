from django.db import models


# Transaction model
class Transaction(models.Model):
    card = models.ForeignKey("cards.Card", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(
        max_length=10,
        choices=[("payment", "Payment"), ("charge", "Charge")],
        default="payment",
    )
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.card} - £{self.amount} on {self.date} ({self.type})"
