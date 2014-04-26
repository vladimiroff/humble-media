from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.ResourceList.as_view(), name='list'),
    url(r'^add/$', views.ResourceCreate.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', views.ResourceDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.ResourceEdit.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.ResourceDelete.as_view(), name='delete'),
)
