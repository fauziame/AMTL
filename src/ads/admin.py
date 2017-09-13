# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ad
# Register your models here.
class AdModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated", "newsletter"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    list_editable = ["title", "newsletter"]
    class meta:
        model = Ad

admin.site.register(Ad, AdModelAdmin)