
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^(?P<publish>[\w-]+)/article/$', views.article_list2, name='article'),

    #url(r'^/category/(?P<slug>[\w-]+)/$', views.cat_list, name='cat'),
    url(r'^create/', views.article_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit', views.article_update, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.article_delete, ),
    url(r'^category/(?P<slug>[\w-]+)/$', views.view_category, name='cat'),

]