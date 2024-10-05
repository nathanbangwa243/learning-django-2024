from django.db import models
from django.contrib.auth.models import AbstractUser
from . import validators


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    class Role(models.TextChoices):
        CREATOR = 'CREATOR'
        SUBSCRIBER = 'SUBSCRIBER'

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=Role.choices)

    def __str__(self):
        return self.username