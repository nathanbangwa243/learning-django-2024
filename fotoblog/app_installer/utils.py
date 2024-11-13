# app_installer/utils.py

import os
from importlib import import_module, reload
from modulefinder import Module
from pprint import pprint

from django.conf import settings
from django.core.management import call_command
from django.urls import path, get_resolver, clear_url_caches, include, URLPattern, URLResolver

from .models import AppConfig
from .apps import AppInstallerConfig

import logging

_logger = logging.getLogger(__name__)


def is_app_registered(app_name):
    return app_name in settings.INSTALLED_APPS


def install_app(app_name):
    app = AppConfig.objects.get(name=app_name)

    if app.is_enabled or app_name in settings.INSTALLED_APPS:
        print(f"The App '{app_name}' is already installed")
        print(f"app.is_installed : {app.is_enabled} \n{settings.INSTALLED_APPS}")
        return

    # Ajouter l'application à INSTALLED_APPS et exécuter la migration
    settings.INSTALLED_APPS.append(app_name)
    # call_command("migrate", app_name)
    app.is_enabled = True
    app.save()


def uninstall_app(app_name):
    app = AppConfig.objects.get(name=app_name)

    if not app.is_enabled or app_name not in settings.INSTALLED_APPS:
        return

    # Supprimer l'application de INSTALLED_APPS
    settings.INSTALLED_APPS.remove(app_name)
    # call_command("migrate", app_name, fake=True)  # Supprime les tables de la base de données
    app.is_enabled = False
    app.save()


def detect_apps():
    project_path = settings.BASE_DIR  # Racine du projet Django
    app_names = []

    # Scanner le répertoire pour les applications
    for dir_name in os.listdir(project_path):
        app_path = os.path.join(project_path, dir_name)
        if os.path.isdir(app_path) and os.path.isfile(os.path.join(app_path, 'apps.py')):
            app_names.append(dir_name)

    # Enregistrer dans le modèle App uniquement les nouvelles applications détectées
    for app_name in app_names:

        # check if app is register in INSTALLED_APPS
        if not is_app_registered(app_name):
            continue

        default_app_description = f"Default Description for '{app_name}'"
        # Enregistrer dans le modèle App uniquement les nouvelles applications détectées
        app, created = AppConfig.objects.get_or_create(
            name=app_name,
            defaults={'description': default_app_description}
        )

        try:
            # check app configuration
            app_config_module = import_module(f'{app_name}.apps')

            app_installer_config = getattr(app_config_module, 'APP_INSTALLER_CONFIG', {})

            auto_install = app_installer_config.get('auto_install', False)


            if auto_install:
                app.is_enabled = True
                app.description = app_installer_config.get('description', default_app_description)
                app.save()

        except ModuleNotFoundError:
            _logger.info(f"Not 'apps' module found inside of '{app_name}' app")

    # Supprimer les applications non détectées dans le répertoire mais présentes dans la base de données
    ghost_apps = AppConfig.objects.exclude(name__in=app_names)

    for app in ghost_apps:
        print(f'[GHOST APP] : {app.name}')


    ghost_apps.delete()

    return app_names


def load_app_urls(app_name):
    print(f"\n[utils.load_app_urls] BEGIN:\n")

    try:
        app_urls = import_module(f'{app_name}.urls')
        url_pattern = path(f'{app_name}/', include(app_urls), name=app_name)
        resolver = get_resolver()

        # Ajouter les URLs à la configuration
        if url_pattern not in resolver.url_patterns:
            resolver.url_patterns.append(url_pattern)

        print(f"[utils.load_app_urls] resolver.url_patterns :")
        pprint(resolver.url_patterns)

        # Forcer le rechargement des caches
        clear_url_caches()

    except ModuleNotFoundError:
        print(f"URL config not found for app '{app_name}'.")


def unload_app_urls(app_name):
    print(f"\n[utils.unload_app_urls] BEGIN:\n")

    resolver = get_resolver()
    app_prefix = f'{app_name}/'
    app_urls_module = f'{app_name}.urls'

    # for pattern in resolver.url_patterns:
    #     # print(type(pattern.pattern), pattern.pattern.name, pattern.pattern)
    #     if isinstance(pattern, URLPattern):
    #         print(type(pattern), pattern.name)
    #     if isinstance(pattern, URLResolver) and pattern.app_name == app_name:
    #         print('[TARGET]', type(pattern), pattern.app_name, type(pattern.app_name))
    #         print(pattern.app_name, app_name, pattern.app_name == app_name, type(app_name))

    # resolver.url_patterns = [
    #     pattern for pattern in resolver.url_patterns
    #     if not (
    #             (isinstance(pattern, URLPattern) and str(pattern.pattern).startswith(app_prefix)) or
    #             (isinstance(pattern, URLResolver) and pattern.app_name == app_name)
    #     )
    # ]

    new_url_patterns = []

    for pattern in resolver.url_patterns:
        # Ignorer les patterns associés à l'app_name
        if isinstance(pattern, URLPattern) and str(pattern.pattern).startswith(app_prefix):
            continue

        if isinstance(pattern, URLResolver) and pattern.app_name == app_name:
            continue

    resolver.url_patterns = new_url_patterns

    # Effacer les caches pour forcer le rechargement
    clear_url_caches()

    print(f"[utils.unload_app_urls] resolver.url_patterns :")
    pprint(resolver.url_patterns)
