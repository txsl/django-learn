from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learn.views.home', name='home'),
    # url(r'^learn/', include('learn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root' : os.path.join(os.path.dirname(__file__), "../tinymce")}),
    (r'^search/$', 'search.views.search'),
    (r'', include('django.contrib.flatpages.urls')),
)
