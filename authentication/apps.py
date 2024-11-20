from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'


# app_installer config
APP_INSTALLER_CONFIG = {
    'auto_install': True,
}