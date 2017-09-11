# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Newsletter
from django.contrib import admin

# Register your models here.

class NLModelAdmin(admin.ModelAdmin):
    list_display = ["publish"]
    inline = ["publish"]

    class meta:
        model = Newsletter

admin.site.register(Newsletter, NLModelAdmin)