import os
from easy_thumbnails.conf import Settings as thumbnail_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8^66oxt=44+*hb+nnnkt9lckf1_y0z4l=worutx&9@ajhl-19e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # local_settings

DOMAIN_NAME = ''  # local_settings

ALLOWED_HOSTS = ['127.0.0.1']  # local_settings

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'image_cropping',
    'easy_thumbnails',
    'web',
    'tour',
    'album',
    'work',
    'member',
    'shop',
    'django_cleanup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CoolkerTour.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CoolkerTour.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {  # local_settings
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '<database>',  # Or path to database file if using sqlite3.
        'USER': '<user>',  # Not used with sqlite3.
        'PASSWORD': '<password>',  # Not used with sqlite3.
        'HOST': '<host>',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '<port>',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'charset': 'utf8mb4'},
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGGING_FOLDER = ''  # local_settings

TEST_SITE = False  # local_settings

VIRTUALENV_PATH = ''  # local_settings

CKEDITOR_JQUERY_URL = 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'img/ckeditor/'
CKEDITOR_BROWSE_SHOW_DIRS = True  # 顯示資料夾
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
    },
}

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

THUMBNAIL_NAMER = 'easy_thumbnails.namers.hashed'

RECAPTCHA_SITE_KEY = ''
RECAPTCHA_SECRET_KEY = ''

LINE_NOTIFY_ACCESS_TOKEN = ''

try:
    from .local_settings import *
except ImportError:
    raise Exception("A local_settings.py file is required to run this project")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_FOLDER + '/default.log',
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 0,  # 備份份數
            'formatter': 'verbose'
        },
        'request': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_FOLDER + '/request.log',
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 備份份數
            'formatter': 'verbose'
        },
        'db': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_FOLDER + '/db.log',
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 1,  # 備份份數
            'formatter': 'verbose'
        },
        'template': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_FOLDER + '/template.log',
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 1,  # 備份份數
            'formatter': 'verbose'
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_FOLDER + '/debug.log',
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 備份份數
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        'line': {
            'level': 'ERROR',
            'class': 'CoolkerTour.logging_handlers.LineAdminHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['request', 'line'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.db': {
            'handlers': ['db'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.template': {
            'handlers': ['template'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'debug': {
            'handlers': ['debug'],
            'propagate': False,
            'level': 'DEBUG',
        },
    }
}
