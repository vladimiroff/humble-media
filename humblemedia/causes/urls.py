from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('causes.views',
    url(r'^list/$', views.CauseList.as_view(), name="cause_list"),
    url(r'^create/$', views.CauseCreate.as_view(), name="cause_create"),
    url(r'^(?P<pk>\d+)/$', views.CauseDetails.as_view(), name="cause_details"),
    url(r'^(?P<pk>\d+)/edit/$', views.CauseUpdate.as_view(), name="cause_edit"),
    url(r'^(?P<pk>\d+)/delete/$', views.CauseDelete.as_view(), name="cause_edit"),
)
