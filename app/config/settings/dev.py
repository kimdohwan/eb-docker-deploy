from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))


ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

DATABASES = secrets['DATABASES']

# ------------------S3 설 정----------------
INSTALLED_APPS += [
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'
STATICFILES_STORAGE = 'config.storages.S3StaticStorage'

AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

# ------------------------------------------