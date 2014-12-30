"""
Django settings for appsoc project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/home/folusoogunlana/Documents/webprogramming/appsoc/appsoc/templates",
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    "/Users/folusoogunlana/Documents/webprogramming/appsoc/static",
)


ALLOWED_HOSTS = [
    'www.icappsoc.co.uk',  # Allow domain and subdomains
    '.icappsoc.co.uk',  # Also allow FQDN and subdomains
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%^*ea%ow0^4+n591su&wgc_me#flsqr+av1zw#cyn!#c95s)db'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# set up mail here


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'foluso311@gmail.com'
EMAIL_HOST_PASSWORD = 'Hoogland92'
DEFAULT_FROM_EMAIL = 'foluso311@gmail.com'
DEFAULT_TO_EMAIL = 'foluso311@gmail.com'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mongoengine.django.mongo_auth',  # MONGOENGINE
    # 'djcelery',  # Celery Async
    'appsoc',
)

# MONGO ENGINE {

AUTH_USER_MODEL = 'mongo_auth.MongoUser'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'

SESSION_ENGINE = 'mongoengine.django.sessions'
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

DEV_URI = None
PROD_URI = 'mongodb://foogunlana:Hoogland92@ds027491.mongolab.com:27491/appsoc'

MONGO_URI = PROD_URI

import mongoengine
mongoengine.connect('appsoc', host=MONGO_URI)

# MONGO ENGINE }

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'appsoc.urls'

WSGI_APPLICATION = 'appsoc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# MONGO ENGINE {

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy'
#     }
# }

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

# MONGO ENGINE }

# CELERY

# CELERY_RESULT_BACKEND = 'mongodb://192.168.1.100:30000/'
# CELERY_MONGODB_BACKEND_SETTINGS = {
#     'database': 'mydb',
#     'taskmeta_collection': 'my_taskmeta_collection',
# }

# appsoc.conf.update(
#     CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
# )

# appsoc.conf.update(
#     CELERY_RESULT_BACKEND='djcelery.backends.cache:CacheBackend',
# )

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
                       "django.contrib.staticfiles.finders.AppDirectoriesFinder")

STATIC_URL = '/static/'
