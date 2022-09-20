from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'users',
        'USER': 'aaaaa@a.com',
        'PASSWORD': 'master',
        'HOST': '127.0.0.1',
        'PORT': '54328',
    }
}
