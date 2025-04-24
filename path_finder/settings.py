import os
from datetime import timedelta
from pathlib import Path

# from corsheaders.defaults import default_headers

import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS")
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")

# Application definition

INSTALLED_APPS = [
    "auth_common.apps.AuthCommonConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework_swagger",
    "drf_yasg",
    "rest_framework_simplejwt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",          # 🔐 First for security headers
    "corsheaders.middleware.CorsMiddleware",                  # 🌍 CORS right after
    "django.contrib.sessions.middleware.SessionMiddleware",   # 🛒 For sessions
    "django.middleware.common.CommonMiddleware",              # 📦 Common features
    "django.middleware.csrf.CsrfViewMiddleware",              # 🛡 CSRF protection
    "django.contrib.auth.middleware.AuthenticationMiddleware",# 👤 Authentication
    "django.contrib.messages.middleware.MessageMiddleware",   # 💬 Messages
    "django.middleware.clickjacking.XFrameOptionsMiddleware", # 🛡 Clickjacking
]


ROOT_URLCONF = "path_finder.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# WSGI_APPLICATION = "path_finder.wsgi.application"
ASGI_APPLICATION = "path_finder.asgi.application"

# SECURITY
# ------------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        # local
        "ENGINE": "django.db.backends.postgresql",
        # staging
        # "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": env("DB_NAME"),
#         "USER": env("DB_USER"),
#         "PASSWORD": env("DB_PASSWORD"),
#         "HOST": env("DB_HOST"),
#         "PORT": env("DB_PORT"),
#     },
# }
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# DATABASES = {
#     "default": {
#         # local
#         # "ENGINE": "django.db.backends.postgresql",
#         # staging
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": 'mysqldb',
#         "USER": 'root',
#         "PASSWORD": 'admin',
#         "HOST": '127.0.0.1',
#         "PORT": '3306',
#     }
# }

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    )
}
APPEND_SLASH = False


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# For Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = env("SERVER_EMAIL")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "auth_common.User"
API_VERSION = "v1"

# Django project settings.py

# JWT setting
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=16),
}

CORS_ALLOWED_ORIGINS = [
    # "https://example.com",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://192.168.1.99:8002",
]
