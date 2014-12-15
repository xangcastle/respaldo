import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Cesar Abel', 'cesarabel@deltacopiers.dyndns.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dd0lkll4l2717a',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'rsujiklxazuzbo',
        'PASSWORD': 'abxYG-a0IR84FV-7zL57a1BgP4',
        'HOST': 'ec2-54-235-83-5.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = ['deltacopiers.dyndns.org']

TIME_ZONE = 'America/Managua'

LANGUAGE_CODE = 'es-NI'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),'media/'))
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # deltacopiers.path.join(deltacopiers.path.dirname(__file__),'static')
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(RUTA_PROYECTO,'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bq7!d7y__xli6w&a-atxf^799bmx-xfyqo3wyyn2*mhs_(bq43'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'recibos.middleware.user.LocalUserMiddleware',
)

ROOT_URLCONF = 'deltacopiers.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'deltacopiers.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'plantillas'),
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    ##INCLUIR LAS SIGUIENTES APLICACIONES DENTRO DE LOS REQUERIMIENTOS
    'adminactions',
    'grappelli_dynamic_navbar',
    'ajax_select',
    'grappelli',
    'import_export',
                  
    ##APLICACIONES BASICAS DEL ADMIN
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'recibos', ## SISTEMA DE CONTROL DE COPIADORAS DE DELTACOPIERS NO TOCAR!
    
    ##APLICACIONES DEL SISTEMA INTEGRADO MONEYCASH##
    'moneycash',
    'moneycash.bodega',
    'moneycash.caja',
    'moneycash.facturacion',
    'moneycash.compras',
    'moneycash.cartera',
    'moneycash.contabilidad',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#import dj_database_url
#DATABASES['default'] = dj_database_url.config()
import django.conf.global_settings as DEFAULT_SETTINGS

CUSTOM_PROCESSORS = ('django.core.context_processors.request',)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + CUSTOM_PROCESSORS

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


###########################################################################

# DEFINE THE SEARCH CHANNELS:

AJAX_LOOKUP_CHANNELS = {
    # simplest way, automatically construct a search channel by passing a dict
    'label': {'model': 'music.label', 'search_field': 'url'},

    # Custom channels are specified with a tuple
    # channel: ( module.where_lookup_is, ClassNameOfLookup )
    'person': ('music.lookups', 'PersonLookup'),
    'group': ('music.lookups', 'GroupLookup'),
    'song': ('music.lookups', 'SongLookup'),
    'cliche': ('music.lookups', 'ClicheLookup'),
    'cliente': ('moneycash.lookups', 'ClienteLookup'),
}


# By default will use window.jQuery
# or Django Admin's jQuery
# or load one from google ajax apis
# then load jquery-ui and a default css
# Set this to False if for some reason you want to supply your own
# window.jQuery and jQuery UI

# AJAX_SELECT_BOOTSTRAP = False


###########################################################################







