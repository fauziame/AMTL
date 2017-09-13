# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from newsletter.models import Newsletter
from django.conf import settings

# Create your models here.

AdTypes = (
        ('a', 'Side Ad'),
        ('b', 'Top Ad'),

    )
def upload_location(instance, filename):

    return "%s/%s" %(instance.id, filename)
class Ad(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=40)
    Ad_Type = models.CharField(max_length=15,choices=AdTypes, null=True, blank=True)
    image = models.ImageField(upload_to="upload_location",null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    url = models.URLField(max_length=200)
    newsletter= models.ForeignKey(Newsletter, null=True, blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title