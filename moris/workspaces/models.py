from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from moris.viewports.models import Viewport

#from moris.conf import settings


class Workspace(models.Model):
    owner = models.ForeignKey(User)
    name  = models.CharField(_('Name'), max_length=50)


class WorkspaceAccess(models.Model):
    workspace = models.ForeignKey(Workspace)
    user = models.ForeignKey(User)
    can_view = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=False)


class WorkspaceViewport(models.Model):
    workspace = models.ForeignKey(Workspace)
    viewport = models.ForeignKey(Viewport)
    pos_x = models.PositiveIntegerField(default=0)
    pos_y = models.PositiveIntegerField(default=0)


class WorkspaceMenuItem(models.Model):
    workspace = models.ForeignKey(Workspace)
    parent = models.ForeignKey('self', blank=True, null=True)
    label = models.URLField(_('URL'), max_length=255)
