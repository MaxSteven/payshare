"""
Django settings for payshare project.

Generated by "django-admin startproject" using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.contrib.staticfiles.apps import StaticFilesConfig


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k4f%dddo44p-ad4q4f#!fq=-1a-7axw9iml+utej%a4z_^%ynu"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "payshare.settings.CustomizedStaticFilesConfig",  # replaces "staticfiles"
    "django.contrib.humanize",

    "corsheaders",
    "rest_framework",

    # django-filer related:
    "easy_thumbnails",
    "filer",
    "mptt",

    "payshare.purchases",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "payshare.purchases.middleware.readonly_middleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Comment next line out if you are not using it, since any middleware
    # may possibly interfer with exceptions bubbling up etc. unwanted.
    # "payshare.purchases.middleware.debugging_middleware",
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "payshare.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Allow loading the Vue app dist/index.html as a template,
            # although it does not reside within an app"s templates/
            # directory. Note: Avoid conflicts with existing app
            # namespaces.
            os.path.join(BASE_DIR),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "payshare.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "public", "media")


class CustomizedStaticFilesConfig(StaticFilesConfig):
    """Ignore some unnecessary folder during " collectstatic"."""
    ignore_patterns = ["node_modules", "cypress"]


STATIC_URL = "/static/"
STATICFILES_DIRS = [
    # Collect build results, like bundle files and service-worker.
    os.path.join(
        BASE_DIR, "payshare", "purchases", "static", "client", "dist"
    )
]
STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365  # One year.

# https://django-filer.readthedocs.io/en/latest/installation.html
THUMBNAIL_HIGH_RESOLUTION = True
ADMIN_MEDIA_PREFIX = "/static/admin/"

CLIENT_APP_TEMPLATE = "payshare/purchases/static/client/dist/index.html"
