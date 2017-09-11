# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from article.models import Article
# Create your models here.


class Header(models.Model):
    main_article = models.ForeignKey(Article, null=True, blank=True, related_name='main_article')
    article_a = models.ForeignKey(Article, null=True, blank=True, related_name='article_a')
    article_b = models.ForeignKey(Article, null=True, blank=True, related_name='article_b')
    article_c = models.ForeignKey(Article, null=True, blank=True, related_name='article_c')
    article_d = models.ForeignKey(Article, null=True, blank=True, related_name='article_d')
    expiration = models.DateField(auto_now=False, auto_now_add=False, null=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return unicode(self.publish)
