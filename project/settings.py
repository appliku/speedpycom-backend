import os
from configurations import Configuration, values
from project.settings_base import ProjectBaseConfig
from datetime import timedelta
from pathlib import Path

# Temporary solution to make sure Django picks up the default auto_field.
# Model checks are performed before django-configurations are instantiated
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


class ProjectConfig(ProjectBaseConfig):
    """
    Check settings_base.py for more settings.
    settings_base.py provides a reasonable set of defaults for a Django project.

    Copy settings into this class to override the defaults.
    """
    """
    Project Apps Definitions
    Django Apps - Django Internal Apps
    Third Party Apps - Apps installed via requirements.txt
    Project Apps - Project owned / created apps

    Installed Apps = Django Apps + Third Part apps + Projects Apps
    """

    DJANGO_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.sites',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.redirects',
        'django.contrib.sitemaps',
    ]

    THIRD_PARTY_APPS = [
        'import_export',
        'django_extensions',
        'rest_framework',
        'rest_framework_simplejwt',
        'rest_framework_simplejwt.token_blacklist',
        'storages',
        'corsheaders',
        'djangoql',
        'post_office',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
        'drf_spectacular',
    ]

    PROJECT_APPS = [
        'usermodel',
        'main',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    SPECTACULAR_SETTINGS = {
        'TITLE': 'SpeedPyCom API',
        'DESCRIPTION': 'API documentation for SpeedPyCom based app',
        'VERSION': '1.0.0',
        'SERVE_INCLUDE_SCHEMA': False,
        'COMPONENT_SPLIT_REQUEST': True,
        # OTHER SETTINGS
    }
