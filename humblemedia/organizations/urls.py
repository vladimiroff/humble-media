from django.conf.urls import patterns, url

urlpatterns = patterns('organizations.views',
    url(r'^add/$', 'add', name='add'),
    url(r'^edit/(?P<pk>\d+)/$', 'edit', name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', 'delete', name='delete'),
)
