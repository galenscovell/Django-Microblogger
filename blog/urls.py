from django.conf.urls import patterns, url, include
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.main_page),
    url(r'^all/$', views.post_list),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail),
    url(r'^new/$', views.post_new),
    url(r'^register/$', views.user_register),
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
)
