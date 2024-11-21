from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


# app_installer config
APP_INSTALLER_CONFIG = {
    'auto_install': False,
}

# print('http://127.0.0.1:8000/blog')
