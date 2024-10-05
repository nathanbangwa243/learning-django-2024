"""
URL configuration for photoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

from django.urls import path

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # authentication apps
    # path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
    ), name='login'),

    # path('logout/', authentication.views.LogoutUserView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(
        next_page='login',
    ), name='logout'),

    path('signup/', authentication.views.SignUpView.as_view(), name='signup'),

    # Changes Password
    path('password-change/',
         PasswordChangeView.as_view(template_name='authentication/password_change.html',
                                    success_url='/password-change-done/'),
         name='password_change'),

    path('password-change-done/',
         PasswordChangeDoneView.as_view(template_name='authentication/change_password_done.html'),
         name='password_change_done'),

    # BLOGS APPS
    path('home/', blog.views.home, name='home'),

]