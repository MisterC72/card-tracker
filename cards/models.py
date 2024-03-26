from django.db import models


# Create a new model called Card
class Card(models.Model):
    provider = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_zero_percent = models.BooleanField(default=False)
    zero_percent_end = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.provider
