# Django settings for mysite project.
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

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
)

MANAGERS = ADMINS

TIME_ZONE = 'Ukraina/Kyiv'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = 'http://my-math.houa.org/Media/'

# URL prefix for admin media -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = '/media/adminmedia/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.SaveAuthenticationRequestMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'mysite.mydata',
)

FIXTURE_DIRS = (
)

DATABASE_SUPPORTS_TRANSACTIONS = True

# Import settings from local_settings.py, if it exists.
try:
    import local_settings
except ImportError:
    print """ 
    -------------------------------------------------------------------------
    You need to create a local_settings.py file which needs to contain at least
    database connection information.
    -------------------------------------------------------------------------
    """
    import sys 
    sys.exit(1)
else:
    # Import any symbols that begin with A-Z. Append to lists any symbols that
    # begin with "EXTRA_".
    import re
    for attr in dir(local_settings):
        match = re.search('^EXTRA_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                globals()[name] += value
            except KeyError:
                globals()[name] = value
        elif re.search('^[A-Z]', attr):
            globals()[attr] = getattr(local_settings, attr)
