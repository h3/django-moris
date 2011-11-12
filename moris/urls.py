from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()
urlpatterns = patterns('',
    (r'^i18n/',      include('django.conf.urls.i18n')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/',     include(admin.site.urls)),
    (r'^workspace$', include('moris.workspaces.urls')),
#   (r'^viewport$',  include('moris.viewport.urls')),
)

if settings.DEV:
    urlpatterns += patterns('', (r'^%s(.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': 'media'}),)

