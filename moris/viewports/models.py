from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Viewport(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    width = models.PositiveIntegerField(default=200)
    height = models.PositiveIntegerField(default=200)
