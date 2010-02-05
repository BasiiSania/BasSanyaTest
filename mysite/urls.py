from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    ('^$', 'mysite.mydata.views.main_page'),
    (r'^editor/$', 'mysite.mydata.views.editor'),
    (r'^accounts/login/$', login),
    (r'^admin/', include(admin.site.urls)),
)
