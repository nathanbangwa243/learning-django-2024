import os
from importlib import import_module, reload

from django.conf import settings
from django.core.management import call_command
from .models import App

def install_app(app_name):
    app = App.objects.get(name=app_name)

    if not app.is_installed or app_name not in settings.INSTALLED_APPS:
        return

    # Ajouter l'application à INSTALLED_APPS et exécuter la migration
    settings.INSTALLED_APPS.append(app_name)
    call_command("migrate", app_name)
    app.is_installed = True
    app.save()

def uninstall_app(app_name):
    app = App.objects.get(name=app_name)
    if not app.is_installed or app_name not in settings.INSTALLED_APPS:
        return

    # Supprimer l'application de INSTALLED_APPS
    settings.INSTALLED_APPS.remove(app_name)
    call_command("migrate", app_name, fake=True)  # Supprime les tables de la base de données
    app.is_installed = False
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
        App.objects.get_or_create(name=app_name, defaults={'description': 'Description par défaut'})

        app = App.objects.get(name=app_name)

        # app already in INSTALLED_APPS
        if app_name in settings.INSTALLED_APPS:
            app.is_installed = True
            app.save()

        else:
            app.is_installed = False
            app.save()

    return app_names