from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'humblemedia.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^organizations/', include('organizations.urls')),
    url(r'^causes/', include('causes.urls')),
)
