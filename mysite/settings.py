# Django settings for mysite project.
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

#TEMPLATE_CONTEXT_PROCESSORS = ('context_processors.django_settings_proc')
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'context_processors.django_settings',
)

ADMINS = (
    ('Oleksandr', 'obasiy@ukr.net'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql',
                               # 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'C:\Documents and Settings\Ingusik\BasSanyaTest\mysite\mydb.db'
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not
                               #   used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not
                               #   used with sqlite3.
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

TIME_ZONE = 'Ukraina/Kyiv'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3p3%gah*_nvf^l8309)hl9$c#lrrv2dr2_eu!cc$qfu*p#ia1('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.SaveAuthenticationRequestMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATE_DIRS = (
    'C:\Documents and Settings\Ingusik\BasSanyaTest\mysite\Templates',
    os.path.join(PROJECT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or
    #   "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'mysite.books',
    'mysite.my_templatetags',
)

FIXTURE_DIRS = (
)

DATABASE_SUPPORTS_TRANSACTIONS = True

#from settings_local import *
#to end
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

INSTALLED_APPS += (
    'debug_toolbar',
# django-coverage 1.0.1
#    'test_coverage',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
INTERNAL_IPS = ('127.0.0.1', )

#TEST_RUNNER = (
#django-coverage 1.0.1
#    'django_coverage.coverage_runner.run_tests',
#)

COVERAGE_CODE_EXCLUDES = (
)

#COVERAGE_REPORT_HTML_OUTPUT_DIR = ''
