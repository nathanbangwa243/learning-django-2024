import os
import dj_database_url

from .base import *

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '')

DATABASE_URL = os.getenv('DATABASE_URL', '')

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.getenv('DB_HOST'),
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }


DATABASES = {
    # 'default': dj_database_url.config(default='postgres://localhost/mydb')
    'default': dj_database_url.config(default=DATABASE_URL)
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add whitenoise.middleware.WhiteNoiseMiddleware to the MIDDLEWARE setting 
# (before django.middleware.common.CommonMiddleware)
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


