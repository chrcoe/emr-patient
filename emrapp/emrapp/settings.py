"""
Django settings for emrapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

ADMIN_MEDIA_PREFIX = '/admin/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# tell Django which User Model to use
AUTH_USER_MODEL = 'patient.Patient'
# /logout clears all session data and redirects to login URL
LOGIN_URL = '/logout'

# Application definition
# all user apps need to be added here to be included in django operations
# such as DB migrations, etc.
USER_APPS = (
    'patient',  # this is the main app we are developing
)

# all built in apps that we want to use... these are modules that come
# with Django
BUILT_IN_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# use both built ins and user apps
INSTALLED_APPS = USER_APPS + BUILT_IN_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'emrapp.urls'

WSGI_APPLICATION = 'emrapp.wsgi.application'


# Database info is stored in the local/prod settings files


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (
#    os.path.join(PROJECT_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'staticfiles'),
    #    os.path.join(BASE_DIR, 'static'),
)

#print (STATICFILES_DIRS)


# media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# extra templates
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'emrapp/templates'),
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

# print(TEMPLATE_DIRS)

# if local_settings.py is in the emrapp/emrapp directory, it is used to
# add local specifics
try:
    from local_settings import *
except ImportError:
    pass

# if prod_settings.py is in the emrapp/emrapp directory, it is used to add
# production specifics
try:
    from prod_settings import *
except ImportError:
    pass
