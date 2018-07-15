from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'storages',
]

WSGI_APPLICATION = 'config.wsgi.dev.application'

secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

DATABASES = secrets['DATABASES']

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

DEFAULT_FILE_STORAGE = 'config.storage.S3DefaultStorage'
STATICFILES_STORAGE = 'config.storage.S3StaticStorage'

AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = secrets['AWS_DEFAULT_ACL']
AWS_S3_REGION_NAME = secrets['AWS_S3_REGION_NAME']
AWS_S3_SIGNATURE_VERSION = secrets['AWS_S3_SIGNATURE_VERSION']
