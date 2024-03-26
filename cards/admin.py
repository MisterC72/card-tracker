from django.contrib import admin

# Add the Card model to the admin site
from .models import Card

admin.site.register(Card)
