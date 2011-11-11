from django.db import models


class Viewport(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    width = models.PositiveIntegerField(default=200)
    height = models.PositiveIntegerField(default=200)
