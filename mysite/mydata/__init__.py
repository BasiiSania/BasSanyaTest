import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

def setup():
    from django.test.utils import setup_test_environment
    setup_test_environment()

def teardown():
    from django.test.utils import teardown_test_environment
    teardown_test_environment()
