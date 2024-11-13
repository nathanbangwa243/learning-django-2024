from faulthandler import is_enabled

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # login
    path('', include('authentication.urls'), name='home'),

    # APPS DASHBOARD
    # path('apps/', include('app_installer.urls'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
