from django.apps import AppConfig


import logging
import pprint

_logger = logging.getLogger(__name__)


class AppInstallerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_installer'

    # def ready(self):
    #     try:
    #         from app_installer.models import App
    #
    #         installed_apps = [app.name for app in App.objects.filter(is_installed=True)]
    #
    #         settings.INSTALLED_APPS += installed_apps
    #
    #     except (OperationalError, ImproperlyConfigured) as e:
    #         print(f"Installed APPS loading error : {e}")
    #
    #     else:
    #         _logger.info("settings.INSTALLED_APPS = %s", pprint.pprint(settings.INSTALLED_APPS))
