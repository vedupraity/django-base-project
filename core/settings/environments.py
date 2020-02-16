import os
from logging import config as logging_config

import dj_database_url
from decouple import config

from .base import BaseSetting


class DevelopmentSetting(BaseSetting):
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    # DJ-Database-URL
    # https://github.com/jacobian/dj-database-url
    DATABASES = {
        'default': dj_database_url.config(
            default='sqlite:///db.sqlite3',
        ),
    }

    SECRET_KEY = config(
        'DJANGO_SECRET_KEY',
        default='8dy+w75egz%4b+fxx%xep0j@p^=#p5i@s%3xpml+_4*b_llbe8',
    )

    LOG_FILE_PATH = config(
        'LOG_FILE_PATH',
        default=os.path.join(BaseSetting.BASE_DIR, 'logs', 'django.log'),
    )

    logging_config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': config('LOGGING_LEVEL', default='DEBUG'),
            'handlers': ['console', 'rotating_file_handler'],
        },
        'formatters': {
            'file': {
                'format': "[%(asctime)s] %(levelname)s "
                          "[%(process)d|%(processName)s] "
                          "[%(name)s|%(funcName)s|%(lineno)s] "
                          "%(message)s [%(pathname)s]",
                'datefmt': "%Y-%m-%d %H:%M:%S %Z",
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
            'rotating_file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'file',
                'filename': LOG_FILE_PATH,
                'maxBytes': 20480,
                'backupCount': 2,
            },
        },
        'loggers': {
            'django': {
                'level': config('LOGGING_LEVEL', default='DEBUG'),
                'handlers': ['console', 'rotating_file_handler'],
                'propagate': False,
            },
        },
    })


class ProductionSetting(BaseSetting):
    DEBUG = False

    ALLOWED_HOSTS = ['*']

    # DJ-Database-URL
    # https://github.com/jacobian/dj-database-url
    DATABASES = {
        'default': dj_database_url.config(
            default='sqlite:///db.sqlite3',
        ),
    }

    SECRET_KEY = config(
        'DJANGO_SECRET_KEY',
        default='lu!n^ajly*a__nkv3&t1rc^9yx((xher2__lz6t&d5x1dt)$tx',
    )

    LOG_FILE_PATH = config(
        'LOG_FILE_PATH',
        default=os.path.join(BaseSetting.BASE_DIR, 'logs', 'django.log'),
    )

    logging_config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': config('LOGGING_LEVEL', default='WARNING'),
            'handlers': ['console', 'rotating_file_handler'],
        },
        'formatters': {
            'file': {
                'format': "[%(asctime)s] %(levelname)s "
                          "[%(process)d|%(processName)s] "
                          "[%(name)s|%(funcName)s|%(lineno)s] "
                          "%(message)s [%(pathname)s]",
                'datefmt': "%Y-%m-%d %H:%M:%S %Z",
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
            'rotating_file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'file',
                'filename': LOG_FILE_PATH,
                'maxBytes': 20480,
                'backupCount': 2,
            },
        },
        'loggers': {
            'django': {
                'level': config('LOGGING_LEVEL', default='WARNING'),
                'handlers': ['console', 'rotating_file_handler'],
                'propagate': False,
            },
        },
    })
