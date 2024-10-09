from tokenize import group

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

from . import validators


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    class Role(models.TextChoices):
        CREATOR = 'CREATOR'
        SUBSCRIBER = 'SUBSCRIBER'

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=Role.choices)

    followers = models.ManyToManyField('self',
                                       limit_choices_to={'role': CREATOR},
                                       symmetrical=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)

        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)
        else:
            pass
