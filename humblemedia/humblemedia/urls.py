from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from . import views


urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^causes/', include('causes.urls', namespace='causes')),
    url(r'^organizations/', include('organizations.urls', namespace='organizations')),
    url(r'^resources/', include('resources.urls', namespace='resources')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^(?P<model>(resources|causes))/(?P<pk>.*)/upload/$', 'resources.views.upload_attachment',
        name='upload-attachment'),
)
