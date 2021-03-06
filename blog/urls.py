from django.conf.urls import patterns, url, include
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.post_list),
    url(r'^about/$', views.about_page),
    url(r'^new/$', views.post_new),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail),
    url(r'^edit/(?P<post_id>[0-9]+)/$', views.post_edit),
    url(r'^delete/(?P<post_id>[0-9]+)/$', views.post_delete),
    url(r'^like/(?P<post_id>[0-9]+)/$', views.post_like),
    url(r'^comment/(?P<post_id>[0-9]+)/$', views.comment_add),
    url(r'^commentup/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)/$', views.comment_upvote),
    url(r'^commentdown/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)/$', views.comment_downvote),
    url(r'^register/$', views.user_register),
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^search/$', views.search),
)
