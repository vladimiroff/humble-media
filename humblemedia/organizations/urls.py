from django.conf.urls import patterns, url

urlpatterns = patterns('organizations.views',
    url(r'^add/', 'add', name='add'),
)
