# production env setting ,later will change the database
from .base import *

DEBUG = False

ADMINs = [
    ('Abhishek Gharami','abhishekgharami1998@gmail.com'),
]


ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
