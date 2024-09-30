# production env setting ,later will change the database
from .base import *
from decouple import config

DEBUG = False

ADMINs = [
    ('Abhishek Gharami','abhishekgharami1998@gmail.com'),
]


ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]
