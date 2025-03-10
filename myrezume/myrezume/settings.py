import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$pcfld0h(!knue!gh3pqc@1n66@1t)vbhr=+4-au348um5ei9='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'cloudinary',
    'cloudinary_storage',
    
    'corsheaders',#server для django react
    'api.apps.ApiConfig', #app
    'rest_framework', #DRF
]

MIDDLEWARE = [
    
    'whitenoise.middleware.WhiteNoiseMiddleware',  #  middleware  для обработки статики
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'corsheaders.middleware.CorsMiddleware',#server для django react перед CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    
    'https://jenyadevelop.pythonanywhere.com',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://rezume-front.vercel.app',# Адрес React-Versel
    'http://127.0.0.1:8001',
    'http://localhost:3000',  # Адрес React-приложения
]
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'myrezume.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../../frontend/app-rezume/build')],
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

WSGI_APPLICATION = 'myrezume.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  
]


STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Медиафайлы
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



STATICFILES_DIRS = [
    
    (BASE_DIR / "../../frontend/app-rezume/build/static").resolve()
]

# Белый шум будет искать файлы в STATIC_ROOT
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = [ 'localhost', '127.0.0.1', 'jenyadevelop.pythonanywhere.com','rezume-front.vercel.app']

CORS_ORIGIN_ALLOW_ALL = True 

# Настройки для Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'diolxlx1v',
    'API_KEY': '941291929461692',
    'API_SECRET': 'hUCy8anjLCBGjH83SPVbgCOSYsA',
}

# Настройка хранения медиафайлов через Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# URL для медиафайлов
# MEDIA_URL = 'CLOUDINARY_URL=cloudinary://<197551772145565>:<wuXhPAEpjXDlcTB8jhUVkSACou4>@diolxlx1v'
MEDIA_URL = 'https://res.cloudinary.com/diolxlx1v/'
# MEDIA_URL = 'https://res.cloudinary.com/<CLOUD_NAME>/'
