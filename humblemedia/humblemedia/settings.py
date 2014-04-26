import os

ALLOWED_HOSTS = []
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True
LANGUAGE_CODE = 'en-us'
ROOT_URLCONF = 'humblemedia.urls'
SECRET_KEY = '5*trcgvuqlu)c+n2665!*-m=xicn$tuitwy4w7rknelpreleg!'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
TEMPLATE_DEBUG = True
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'humblemedia.wsgi.application'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    "humblemedia/templates/",
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'humblemedia/static'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'taggit',
    'crispy_forms',

    'accounts',
    'payments',
    'resources',
    'causes',
    'organizations',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

try:
    from .local_settings import *
except ImportError:
    exit("local_settings.py NOT found!")
