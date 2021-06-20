import os
import dj_database_url
import django_heroku
if os.environ.get('REDIS_URL'):
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "ssl_cert_reqs": None
            },
        }
    }
}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = os.environ.get('DJANGO_DEBUG', True)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# настройки для вконтакте
VK_APP_ID = os.environ.get('VK_APP_ID', '')
VKONTAKTE_APP_ID = VK_APP_ID
SOCIAL_AUTH_VK_OAUTH2_KEY = VK_APP_ID

VK_API_SECRET = os.environ.get('VK_API_SECRET', '')
VKONTAKTE_APP_SECRET = VK_API_SECRET
SOCIAL_AUTH_VK_OAUTH2_SECRET = VK_API_SECRET

ALLOWED_HOSTS = ['127.0.0.1', 'nepokupai.ru', 'localhost', '192.168.0.197', '.herokuapp.com']

LOGIN_REDIRECT_URL = 'account:dashboard'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_STORAGE = 'dontbuyit.storage.WhiteNoiseStaticFilesStorage'

AUTH_USER_MODEL = 'auth.User'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'account.authentication.EmailAuthBackend',
                           'social_core.backends.vk.VKOAuth2',
                           ]

INSTALLED_APPS = [
    'channels',
    'chat',
    'main',
    'items',
    'account',
    'taggit',
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'cloudinary',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_extensions',
    'mathfilters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'dontbuyit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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


WSGI_APPLICATION = 'dontbuyit.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dontbuyit',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    'main/static',
    'account/static',
    'items/static',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

ASGI_APPLICATION = "dontbuyit.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            # "hosts": [os.environ.get('REDIS_URL', ('127.0.0.1', 6379))],
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}

django_heroku.settings(locals())

if os.environ.get('REDIS_URL'):
    cloudinary.config(
      cloud_name="hachlwujp",
      api_key=os.environ.get('cloudinary_api_key', ''),
      api_secret=os.environ.get('cloudinary_api_secret', '')
    )
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
