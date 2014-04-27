from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.ResourceList.as_view(), name='list'),
    url(r'^add/$', views.ResourceCreate.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', views.ResourceDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.ResourceEdit.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.ResourceDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/buy/$', views.ResourceBuy.as_view(), name='buy'),
    url(r'^(?P<pk>\d+)/download/$', views.download, name='download'),
    url(r'^(?P<pk>\d+)/download/(?P<attachment_id>\d+)/$', views.download_attachment, name='download_attachment'),
)
