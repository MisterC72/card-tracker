from django.contrib.auth.models import AbstractUser
from django.db import models


# custom user model
class CustomUser(AbstractUser):
    # add additional fields in here
    nickname = models.CharField(max_length=100, blank=True)
