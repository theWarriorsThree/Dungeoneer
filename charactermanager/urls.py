from django.conf.urls import patterns, include, url, handler404, handler500
from . import views

urlpatterns = patterns('',
    url(r'^$', views.campaigns),
    url(r'^c/(?P<campaign_name>[\w-]+)/$', views.campaign),
    url(r'^c/(?P<campaign_name>[\w-]+)/(?P<player_name>[\w-]+)/$', views.abilities),
    url(r'^dm/mm/$', views.monsters),
    #url(r'^dm/player/add',views.edit_user),
)

handler404 = 'views.handler404'
handler500 = 'views.handler500'
