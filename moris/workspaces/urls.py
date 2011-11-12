from django.conf.urls.defaults import *
from django.conf import settings

from moris.workspaces.views import *

urlpatterns=patterns('',
    url(r'^$',     WorkspaceView.as_view(), name='moris-workspace'),
)
