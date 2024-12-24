SECRET_KEY = 'django-insecure-d$p98pyx)_w@hdmujpef^hc$7u!pfk=p=+!ldgg!4@0@#w*d5^'

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'DDD.context.urls'

WSGI_APPLICATION = 'DDD.context.wsgi.application'

STATIC_URL = 'static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}