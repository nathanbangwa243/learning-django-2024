from django.contrib import admin

from .models import Blog, Photo

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'starred')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploader', 'date_created')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Photo, PhotoAdmin)