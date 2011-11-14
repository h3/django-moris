from django.conf.urls.defaults import *
from django.conf import settings

from moris.workspaces.views import *

urlpatterns=patterns('',
    url(r'^workspace$', WorkspaceView.as_view(), name='moris-workspace'),
    url(r'^tree$',      TreeTestView.as_view(), name='moris-treetest'),
)
