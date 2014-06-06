"""
Django settings for djangozfs project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'am!&%j9oid05^uttfg^77m+1--#rmrql_z!dxugrfy_u6oq!(w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TOOLBAR_DEBUG = True

TOOLBAR_DEBUG_OVERRIDE = True

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
    #'debug_toolbar.apps.DebugToolbarConfig',
    'kombu.transport.django',
    'design',
    'zfs',
    'disks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'djangozfs.urls'

WSGI_APPLICATION = 'djangozfs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

BROKER_URL = 'django://'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'djangozfs.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

try:
    import debug_toolbar
    ENABLE_DEBUG_TOOLBAR = TOOLBAR_DEBUG
except ImportError:
    ENABLE_DEBUG_TOOLBAR = False
def custom_show_toolbar(request):
    if not ENABLE_DEBUG_TOOLBAR:
            return False
    if not request.user.is_superuser and not TOOLBAR_DEBUG_OVERRIDE:
            print "1!"
            return False
    if 'q' in request.POST and request.POST.get('q', False) == 'debug':
	    print "2!"
            request.POST = request.POST.copy()
            del request.POST['q']
            return True
    if 'q' in request.GET and request.GET.get('q', False) == 'debug':
            print "3!"
            request.GET = request.GET.copy()
            del request.GET['q']
            return True
    return False

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': '%s.custom_show_toolbar' % __name__,
    'ENABLE_STACKTRACES' : True,
    'SHOW_TEMPLATE_CONTEXT': True,
}

CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)
