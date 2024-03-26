from django.contrib import admin

# Add Custom User model to the admin site
from .models import CustomUser


# Display username and email in the admin site
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "is_superuser"]


# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
