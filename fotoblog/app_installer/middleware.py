from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from django.db.utils import OperationalError
from django.core.exceptions import ImproperlyConfigured


import logging
import pprint

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
