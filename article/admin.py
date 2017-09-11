# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated", "newsletter"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    list_editable = ["title", "newsletter"]
    class meta:
        model = Article

admin.site.register(Article, ArticleModelAdmin)

class CatModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inline = ["name"]

    class meta:
        model = Category

admin.site.register(Category, CatModelAdmin)