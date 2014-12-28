from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.campaigns),
    url(r'^(?P<campaign_name>\w+)/$', views.campaign),
    url(r'^(?P<campaign_name>\w+)/(?P<player_name>\w+)/$', views.abilities),
)
