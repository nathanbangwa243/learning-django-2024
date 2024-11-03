from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import App
from .utils import install_app, uninstall_app, detect_apps


class AppDashboardView(View):
    template_name = "app_installer/app_dashboard.html"

    def get(self, request):
        detect_apps()

        apps = App.objects.all()

        return render(request,
                      template_name=self.template_name,
                      context={'apps': apps})

    def post(self, request):
        pass

class InstallAppView(View):
    def get(self, request, app_name):
        install_app(app_name)
        return redirect("app_installer:app_dashboard")

    def post(self, request):
        pass


class UninstallAppView(View):
    def get(self, request, app_name):
        uninstall_app(app_name)
        return redirect("app_installer:app_dashboard")

    def post(self, request):
        pass








