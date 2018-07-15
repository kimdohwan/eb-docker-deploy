from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'class.ap-northeast-2.elasticbeanstalk.com',
    # '172.31.23.203',
]

WSGI_APPLICATION = 'config.wsgi.production.application'




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))
DATABASES = secrets['DATABASES']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

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