from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_installed = models.BooleanField(default=False)
    dependencies = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.name
