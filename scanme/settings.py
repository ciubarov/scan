"""
Django settings for scanme project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7@ql)90q#z+w!ml5lld4g0n2yl0w(fg)xheh2*!s3*uily&++j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'api',
    'app'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.instagram.InstagramOAuth2',
    'social.backends.vk.VKOAuth2',
    'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.core.context_processors.request',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'scanme.urls'

WSGI_APPLICATION = 'scanme.wsgi.application'

SOCIAL_AUTH_FACEBOOK_KEY = '606473496178929'
SOCIAL_AUTH_FACEBOOK_SECRET = '19b3ba844225f92ab0629c872296eeff'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# SOCIAL_AUTH_INSTAGRAM_KEY = 'a616d6731f084c3ebc45ad31378d1e25'
# SOCIAL_AUTH_INSTAGRAM_SECRET = 'bb44cf8f41424defb19784d8f72b728d'

SOCIAL_AUTH_VK_OAUTH2_KEY = '5571721'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'wrW8Agtr7x1JMobNPGgQ'

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY = '1247766528'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET = 'CBAJGQFLEBABABABA'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME = '6DCFAC9A5B92B2A71717BCCA'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)