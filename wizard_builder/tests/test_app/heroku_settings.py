import os

import dj_database_url
from wizard_builder.tests.test_app.settings import *

DEBUG = False

DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL')),
}

MIDDLEWARE_CLASSES = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE_CLASSES

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

ALLOWED_HOSTS = [
    APP_URL,
    os.getenv('HEROKU_APP_NAME', default=''),
    os.getenv('HEROKU_PARENT_APP_NAME', default=''),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%I:%M %p %A(%d) %B(%m) %Y %Z',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': os.getenv('LOG_LEVEL', default='DEBUG'),
        },
        'django.template': {
            'handlers': ['console'],
            'propagate': False,
            'level': os.getenv('LOG_LEVEL', default='INFO'),
        },
    },
    # controls the base log level, set like LOG_LEVEL='ERROR'
    'root': {
        'handlers': ['console'],
        'level': os.getenv('LOG_LEVEL', default='DEBUG'),
    },
}