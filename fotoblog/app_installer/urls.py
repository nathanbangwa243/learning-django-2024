from django.urls import path

from . import views

app_name = "app_installer"

urlpatterns = [
    path("", views.AppDashboardView.as_view(), name='app_dashboard'),
    path("install/<str:app_name>/", views.InstallAppView.as_view(), name='install_app'),
    path("uninstall/<str:app_name>/", views.UninstallAppView.as_view(), name='uninstall_app'),
    path("default-home/<str:app_name>/", views.DefaultAppHomeView.as_view(), name='default_home'),
]