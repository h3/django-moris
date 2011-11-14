import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from moris.workspaces.models import *

class TreeTestView(TemplateView):
    template_name = 'workspaces/treetest.html'


class WorkspaceView(TemplateView):
    template_name = 'workspaces/index.html'
    def get_context_data(self, **kwargs):
        context = super(WorkspaceView, self).get_context_data(**kwargs)
        context['workspace_list'] = Workspace.objects.filter(owner__id=self.request.user.id)
        return context
 
