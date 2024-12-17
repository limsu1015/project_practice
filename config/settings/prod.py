from config.settings.base import *
from dotenv import dotenv_values

ENV = dotenv_values("../../env.prod")

SECRET_KEY = ENV.get('SECRETE_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ENV["ALLOWED_HOSTS"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'