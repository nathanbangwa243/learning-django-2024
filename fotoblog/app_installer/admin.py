from django.contrib import admin

from .models import AppConfig

class AppConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_enabled')


admin.site.register(AppConfig, AppConfigAdmin)