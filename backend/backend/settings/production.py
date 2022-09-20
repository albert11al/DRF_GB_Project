from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'users',
        'USER': 'aaaaa@a.com',
        'PASSWORD': 'master',
        'HOST': 'db',
        'PORT': '5432',
    }
}
