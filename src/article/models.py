# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
# from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from newsletter.models import Newsletter
# from companys.models import Business, Category

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse("articles:cat", kwargs={"slug": self.slug})

class ArticleManager(models.Manager):
    def active(self,*args,**kwargs):
        return super(ArticleManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):

    return "%s/%s" %(instance.id, filename)

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)
    cat = models.ForeignKey(Category, null=True, blank=True)
    image = models.ImageField(upload_to="upload_location",null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    newsletter = models.ForeignKey(Newsletter, null=True, blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = ArticleManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse("articles:edit", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_ad_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_ad_receiver, sender=Article)

