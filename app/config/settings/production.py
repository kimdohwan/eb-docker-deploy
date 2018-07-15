from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com',
]

WSGI_APPLICATION = 'config.wsgi.production.application'

# DB(AWS RDS)
secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))
DATABASES = secrets['DATABASES']

# UPLOAD FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.join(ROOT_DIR, '.media'), 'production')

# STATIC FILES
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

# S3 사용하지 않는다
# STATICFILE_STORAGE = 'config.storage.S3StaticStorage'
# DEFAULT_FILE_STORAGE = 'config.storage.S3DefaultStorage'


# LOG_DIR = '/var/log/django'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'formatters': {
#         'django.server': {
#             'format': '[%(asctime)s] %(message)s',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         },
#         'file_error': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'level': 'ERROR',
#             'formatter': 'django.server',
#             'backupCount': 10,
#             'filename': os.path.join(LOG_DIR, 'error.log'),
#             'maxBytes': 10485760,
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file_error'],
#             'level': 'INFO',
#             'propagate': True,
#         }
#     }
# }