from http.client import responses

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from django.db.utils import OperationalError
from django.core.exceptions import ImproperlyConfigured

from django.urls import get_resolver, get_urlconf, set_urlconf, path, include
from app_installer.models import AppConfig

from importlib import import_module


import logging
from pprint import pprint

_logger = logging.getLogger(__name__)

class DynamicAppLoaderMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.apps_loaded = False


    def __call__(self, request):
        if not self.apps_loaded:
            self.load_dynamic_apps()
            self.apps_loaded = True

        return self.get_response(request)

    def load_dynamic_apps(self):
        try:
            from app_installer.models import App

            installed_apps = [app.name for app in App.objects.filter(is_installed=True)]

            settings.INSTALLED_APPS += installed_apps

        except (OperationalError, ImproperlyConfigured) as e:
            print(f"Installed APPS loading error : {e}")

        else:
            print("The middleware works")
            _logger.info("settings.INSTALLED_APPS = \n%s", pprint.pprint(settings.INSTALLED_APPS))


class DynamicAppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.dynamic_urlpatterns = self.load_dynamic_urls()

    def load_dynamic_urls(self):
        print(f"[DynamicAppMiddleware.load_dynamic_urls] Call")
        # Charger dynamiquement les URLs des applications activées
        dynamic_patterns = []
        for app_config in AppConfig.objects.filter(is_enabled=True):
            try:
                app_urls = import_module(f'{app_config.name}.urls')
                dynamic_patterns.append(path(f'{app_config.name}/', include(app_urls), name=app_config.name))
            except ModuleNotFoundError:
                print(f"URL config not found for app '{app_config.name}'")

        print(f"[DynamicAppMiddleware.load_dynamic_urls] dynamic_patterns :")
        pprint(dynamic_patterns)
        return dynamic_patterns

    def __call__(self, request):
        # Assigner les patterns dynamiques pour chaque requête
        urlconf = get_urlconf()
        resolver = get_resolver(urlconf)

        # Ajouter dynamiquement les URLs si elles ne sont pas déjà ajoutées
        if not any(pattern in resolver.url_patterns for pattern in self.dynamic_urlpatterns):
            resolver.url_patterns.extend(self.dynamic_urlpatterns)

        response = self.get_response(request)
        return response




















