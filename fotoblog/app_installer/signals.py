from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AppConfig
from django.urls import get_resolver, clear_url_caches, include, path
from importlib import import_module

@receiver(post_save, sender=AppConfig)
def update_url_patterns(sender, instance, **kwargs):
    print(f"\n[signals.update_url_patterns] BEGIN:\n")

    # Charger les URL actuelles
    resolver = get_resolver()

    # Filtrer les applications activées
    active_apps = AppConfig.objects.filter(is_enabled=True)

    # Reconstruire les `url_patterns`
    new_url_patterns = []
    for app in active_apps:
        try:
            # Importer le module des URLs de l'application
            app_urls = import_module(f"{app.name}.urls")
            # Ajouter le pattern de l'app avec un préfixe
            new_url_patterns.append(path(f"{app.name}/", include(app_urls)))
        except ModuleNotFoundError:
            continue

    # Mettre à jour les `url_patterns`
    resolver.url_patterns = new_url_patterns
    clear_url_caches()  # Forcer le rechargement des caches pour appliquer les nouvelles URLs

    print(f"\n[signals.update_url_patterns] END:\n")
