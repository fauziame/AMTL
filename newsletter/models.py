# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Newsletter(models.Model):
    expiration = models.DateField(auto_now=False, auto_now_add=False, null=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return unicode(self.publish)

    class Meta:
        ordering = ["-publish", "-updated"]