from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from app_installer.models import AppConfig


class HomeView(View):
    app_name = 'payroll'
    template_name = "payroll/home.html"


    def get(self, request):
        app = AppConfig.objects.get(name=self.app_name)

        if not app.is_enabled:
            return redirect('payroll:forbidden')

        apps = AppConfig.objects.all()

        return render(request,
                      template_name=self.template_name,
                      context={'apps': apps})

    def post(self, request):
        pass

class PayrollForbiddenView(View):
    app_name = 'payroll'
    template_name = 'payroll/forbidden.html'

    def get(self, request):
        return render(request,
                      template_name=self.template_name,
                      context={})