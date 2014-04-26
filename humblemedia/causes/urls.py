from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('causes.views',
    url(r'^create/', views.CauseCreate.as_view(), name="cause_create"),
    url(r'^(?P<pk>\d+)/', views.CauseDetails.as_view(), name="cause_details"),
    url(r'^(?P<pk>\d+)/edit/', views.CauseEdit.as_view(), name="cause_edit"),

)
