from pathlib import Path

import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)  # Set default values and types
)

# Load the .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Use environment variables
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

# Example for the database
DATABASES = {
    'default': env.db(),  # Parses DATABASE_URL
}

# Example for allowed hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')  # Splits comma-separated strings into a list


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_installer',
    'payroll',
    'authentication',
    'blog',
    'invoicing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app_installer.middleware.DynamicAppMiddleware',
]

ROOT_URLCONF = 'fotoblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fotoblog.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        },
    },
    {
        'NAME': 'authentication.validators.ContainsLetterValidator',
    },
    {
        'NAME': 'authentication.validators.ContainsNumberValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'