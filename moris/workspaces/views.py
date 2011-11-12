import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from moris.workspaces.models import *



class WorkspaceView(TemplateView):
    template_name = 'workspaces/index.html'
#   def get_context_data(self, **kwargs):
#       context = super(HomeView, self).get_context_data(**kwargs)
#       #context['object_list'] = ...
#       return context
 
