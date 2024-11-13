from django.urls import path

from . import views

app_name = "payroll"

urlpatterns = [
    path("", views.HomeView.as_view(), name='payroll'),
    path("forbidden/", views.PayrollForbiddenView.as_view(), name='forbidden'),

]