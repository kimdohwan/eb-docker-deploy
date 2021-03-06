import sys

from .base import *

print(sys.argv)

DEBUG = False

secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']
RUNSERVER = 'runserver' in sys.argv
if RUNSERVER:
    DEBUG = True
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
    ]

WSGI_APPLICATION = 'config.wsgi.production.application'

DATABASES = secrets['DATABASES']

# # ------------------S3 설 정----------------
INSTALLED_APPS += [
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'
# STATICFILES_STORAGE = 'config.storages.S3StaticStorage'

AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

# # ------------------------------------------


LOG_DIR = '/var/log/django'

# 에러폴더 만들기 다양한 방법1
# ROOT_LOG = os.path.join(ROOT_DIR, '.log')
#
# if not os.path.exists(LOG_DIR):
#     if not os.path.exists(ROOT_LOG):
#         os.makedirs(f'{ROOT_DIR}/.log')
# 에러폴더 만들기 다양한 방법2
# if not os.path.exists(LOG_DIR):
#     LOG_DIR = os.path.join(ROOT_DIR, '.log')
#     if not os.path.exists(LOG_DIR):
#         os.mkdir(LOG_DIR)
# 에러폴더 만들기 다양한 방법3
if not os.path.exists(LOG_DIR):
    LOG_DIR = os.path.join(ROOT_DIR, '.log')
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'django.server',
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
