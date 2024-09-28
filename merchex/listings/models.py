from contextlib import nullcontext

from django.db import models
from django.db.models import fields
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        GOSPEL = 'GP'
        SLOW = 'SL'

    name = fields.CharField(max_length=100)
    genre = fields.CharField(choices=Genre.choices, max_length=10)
    biography = fields.CharField(max_length=1000)
    year_formed = fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = fields.BooleanField(default=True)
    official_homepage = fields.URLField(null=True, blank=True)

    # manual error
    # limited_edition = fields.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = "REC"
        CLOTHING = "CLO"
        POSTERS = "POS"
        MISCELLANEOUS = "MIS"

    title = fields.CharField(max_length=100)
    description = fields.CharField(max_length=1000)
    sold = fields.BooleanField(default=False)
    year = fields.IntegerField(
        validators=[MinValueValidator(1700), MaxValueValidator(2024)],
        null=True,
        blank=True
    )

    type = fields.CharField(choices=Type.choices, max_length=5)

    # Foreign Keys
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    # manual error
    # limited_edition = fields.BooleanField(default=False)
    # antiquity = fields.BooleanField(default=False)
