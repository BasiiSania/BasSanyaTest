from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from django.contrib import admin

from mysite.views import hello, current_datetime, main_page
from mysite.books import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

admin.autodiscover()


urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^$', main_page),
    (r'^accounts/login/$', login),
    (r'^search/$', views.search),
    (r'^editor/$', views.editor),
    (r'^admin/', include(admin.site.urls)),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
