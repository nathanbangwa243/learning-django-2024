from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import AppConfig
from .utils import install_app, uninstall_app, detect_apps, load_app_urls, unload_app_urls
from .apps import AppInstallerConfig

class AppDashboardView(View):
    template_name = "app_installer/app_dashboard.html"

    def get(self, request):
        detect_apps()

        apps = AppConfig.objects.all()

        return render(request,
                      template_name=self.template_name,
                      context={'apps': apps, 'app_installer': AppInstallerConfig.name})

    def post(self, request):
        pass

class DefaultAppHomeView(View):
    template_name = 'app_installer/default_home.html'

    def get(self, request, app_name):
        app =  AppConfig.objects.get(name=app_name)

        return render(request,
                      template_name=self.template_name,
                      context={'app': app})

    def post(self, request):
        pass

class InstallAppView(View):
    def get(self, request, app_name):
        print(f"\n[InstallAppView.get] BEGIN:\n")
        # install_app(app_name)
        app = AppConfig.objects.get(name=app_name)

        app.enable_app()

        # load app urls
        load_app_urls(app_name)

        print(f"[InstallAppView.get] enable '{app_name}' - state : {app.is_enabled}")

        return redirect("app_installer:app_dashboard")

    def post(self, request):
        pass


class UninstallAppView(View):
    def get(self, request, app_name):
        print(f"\n[UninstallAppView.get] BEGIN:\n")

        # uninstall_app(app_name)
        app = AppConfig.objects.get(name=app_name)

        app.disable_app()

        # unload app urls
        unload_app_urls(app_name)

        return redirect("app_installer:app_dashboard")

    def post(self, request):
        pass


class AppForbiddenView(View):
    template_name = 'app_installer/forbidden.html'

    def get(self, request, app_name):
        app = AppConfig.objects.get(name=app_name)

        return render(request,
                      template_name=self.template_name,
                      context={'app': app})



