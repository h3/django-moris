from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from moris.workspaces.models import *


class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)
    list_filter = ('owner__username',)
    search_fields = ('name', 'owner__username')
admin.site.register(Workspace, WorkspaceAdmin)

