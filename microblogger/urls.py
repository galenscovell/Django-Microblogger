from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
)

urlpatterns += patterns('',
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.MEDIA_ROOT}))