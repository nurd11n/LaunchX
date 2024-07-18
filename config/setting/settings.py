from pathlib import Path
from decouple import config
import os
from django.utils.translation import gettext_lazy as _
from .jazzmine import *
from .logging import *
from .allauth_settings import *
from .installed_apps import *
from .rest_framework import *
from .celery_settings import *
from .spectacular import *
from .cashes import *
from .ckeditor import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config("DEBUG", default=False)

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'users.User'

TOKEN_MODEL = None

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

SITE_ID = 1

if config("DEBUG") == "False":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASS'),
            'HOST': config('DB_HOST', 'history-postgres'),
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
    ("ky", _("Кыргызча")),
)

STATIC_URL = "/back-static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back-static")

MEDIA_URL = '/back-media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "back-media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = ['GЕT', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['Authorization', 'Content-Type']

CSRF_TRUSTED_ORIGINS=["http://127.0.0.1:8000/", 'http://34.159.205.4']

def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

SOCIALACCOUNT_ADAPTER = 'users.adapters.SocialAccountAdapter'
