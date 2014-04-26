from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('causes.views',
    url(r'^list/$', views.CauseList.as_view(), name="list"),
    url(r'^add/$', views.CauseCreate.as_view(), name="add"),
    url(r'^(?P<pk>\d+)/$', views.CauseDetails.as_view(), name="details"),
    url(r'^(?P<pk>\d+)/edit/$', views.CauseUpdate.as_view(), name="edit"),
    url(r'^(?P<pk>\d+)/delete/$', views.CauseDelete.as_view(), name="edit"),
)
