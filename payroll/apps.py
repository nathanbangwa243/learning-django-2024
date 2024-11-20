from django.apps import AppConfig


class PayrollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payroll'

# app_installer config
APP_INSTALLER_CONFIG = {
    'auto_install': False,
}
