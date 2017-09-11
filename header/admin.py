# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Header
from django.contrib import admin

# Register your models here.

class HeadModelAdmin(admin.ModelAdmin):
    list_display = ["publish"]
    inline = ["publish"]

    class meta:
        model = Header

admin.site.register(Header, HeadModelAdmin)