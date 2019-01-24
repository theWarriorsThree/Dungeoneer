from django.conf.urls import include, url, handler404, handler500
from . import views

urlpatterns = [
    url(r'^$', views.campaigns, name="campaigns"),
    url(r'^c/(?P<campaign_name>[\w-]+)/$', views.campaign, name="campaign"),
    url(r'^c/(?P<campaign_name>[\w-]+)/(?P<player_name>[\w-]+)/$', views.abilities, name="abilities"),
    url(r'^dm/mm/$', views.monsters),
    #url(r'^dm/player/add',views.edit_user),
]

handler404 = 'views.handler404'
handler500 = 'views.handler500'
