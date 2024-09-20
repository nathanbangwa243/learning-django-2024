from django.db import models
from django.db.models import fields

class Band(models.Model):
    name = fields.CharField(max_length=100)

class Listing(models.Model):
    title = fields.CharField(max_length=100)