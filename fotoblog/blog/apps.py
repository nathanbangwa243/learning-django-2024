from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


# app_installer config
APP_INSTALLER_CONFIG = {
    'auto_install': False,
}
