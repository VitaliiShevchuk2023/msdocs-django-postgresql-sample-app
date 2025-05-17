import os

from .settings import *  # noqa
from .settings import BASE_DIR

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = False

APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=255b5d65-4b45-498c-b124-41b283997035;IngestionEndpoint=https://westeurope-5.in.applicationinsights.azure.com/;LiveEndpoint=https://westeurope.livediagnostics.monitor.azure.com/;ApplicationId=153ed492-7484-492c-a4b4-abb37de2a9de"

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#
#
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': os.environ['AZURE_POSTGRESQL_NAME'],
         'HOST': os.environ['AZURE_POSTGRESQL_HOST'],
         'USER': os.environ['AZURE_POSTGRESQL_USER'],
         #'PASSWORD': os.environ['AZURE_POSTGRESQL_PASSWORD'],
         'PASSWORD':'lgow2r$TtcKlWy$5', 
         'OPTIONS': {'sslmode': 'require'},
     }
 }

#
#
CACHES = {
         "default": {  
             "BACKEND": "django_redis.cache.RedisCache",
             "LOCATION": os.environ['AZURE_REDIS_CONNECTIONSTRING'],
             "OPTIONS": {
                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
                 "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
         },
     }
}
