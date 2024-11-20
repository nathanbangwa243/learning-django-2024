# Conditions

Here are the conditions for a directory to be considered as an app

**1. Directory must have `app.py` file**

**2. the `app.py` file can contain this configuration**

```python
# my_app/apps.py

# app_installer config

APP_INSTALLER_CONFIG = {
    'auto_install': False,
}
```

**3. Directory must have `urls.py` file**

**4. In the `urls.py` file, the `urlpatterns` must contain one route (`path`) with `directory name` as route (path) name**

```python
# my_app/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='my_app'),

]
```

**5. redirect to dashboard after login**

```python
# project_name/project_name/settings.py

...
LOGIN_REDIRECT_URL = 'app_installer:app_dashboard'
...
```

## Restrict access to the app views

Access to a view can be restricted like this :

```python
# fotoblog\blog\views.py

from .apps import BlogConfig


def home(request):
    # check if app is installed
    app = AppConfig.objects.get(name=BlogConfig.name)

    if not app.is_enabled:
        return redirect('app_installer:forbidden', app_name=BlogConfig.name)
```