from django.db import models

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import clear_url_caches


class AppConfig(models.Model):
    class Meta:
        permissions = [
            ('can_access_app', 'Can access the app'),
        ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_enabled = models.BooleanField(default=False)
    dependencies = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        clear_url_caches()  # Effacer le cache des URLs pour appliquer les changements dynamiques

    def enable_app(self):
        """Enable the app and assign permissions."""
        self.is_enabled = True
        self.save()
        # Logique pour ajouter des permissions à un groupe ou utilisateur spécifique, si nécessaire

    def disable_app(self):
        """Disable the app and revoke permissions."""
        self.is_enabled = False
        self.save()
        # Logique pour retirer les permissions
