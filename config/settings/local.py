from config.settings.base import *
from dotenv import dotenv_values

ENV = dotenv_values('../../envs.local')

SECRET_KEY = ENV.get('SECRETE_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': ENV.get('POSTGRES_HOST', 'localhost'),
        'NAME': ENV.get('POSTGRES_DBNAME', 'oz_practice'),
        'USER': ENV.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': ENV.get('POSTGRES_PASSWORD', 'postgres'),
        'PORT': ENV.get('POSTGRES_PORT', '5432'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'