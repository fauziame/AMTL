# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .models import Category
from .forms import ArticleForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from header.models import Header
# from comments.forms import CommentForm
# from comments.models import Comment
# from companys.models import Business, Category
from django.contrib.contenttypes.models import ContentType
from el_pagination.decorators import page_template

# Create your views here.





def article_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated():
        raise Http404
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created", extra_tags="msg")
        return HttpResponseRedirect(instance.get_absolute_url())
    category_list = Category.objects.all()

    context = {
        "form": form,
        "category_list": category_list

    }
    return render(request,"ad_form.html", context)

def article_detail(request, slug):
    instance = get_object_or_404(Article, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    category_list = Category.objects.all()
    context = {
        "title": instance.title,
        "instance": instance,
        "category_list": category_list,
    }
    return render(request, "article_detail.html", context )

def article_list(request):
    today = timezone.now().date()
    queryset_list = Article.objects.active()


    if request.user.is_superuser or request.user.is_staff:
        queryset_list = Article.objects.all()

    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    category_list = Category.objects.all()

    header = Header.objects.latest("publish")

    context = {
        "articles_list": queryset,
        "title": "List",
        "today": today,
        "category_list": category_list,
        "header":header,

    }

    return render(request, "index.html", context)

def article_list2(request):
    today = timezone.now().date()
    queryset_list = Article.objects.active()


    if request.user.is_superuser or request.user.is_staff:
        queryset_list = Article.objects.all()

    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    category_list = Category.objects.all()

    header = Header.objects.latest("publish")

    context = {
        "articles_list": queryset,
        "title": "List",
        "today": today,
        "category_list": category_list,
        "header":header,

    }

    return render(request, "article.html", context)

def view_category(request,slug):
    category_list = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    queryset_list = Article.objects.active().filter(cat=category)
    if request.user.is_superuser or request.user.is_staff:
        queryset_list = Article.objects.filter(cat=category)

    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    header = Header.objects.all()

    context = {
        'ads_list': queryset_list,
        "category_list": category_list,
    }
    return render(request, 'cat.html', context)





def article_update(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")

        return HttpResponseRedirect(instance.get_absolute_url())
    category_list = Category.objects.all()

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
        "category_list": category_list

    }
    return render(request, "article_form.html", context)

def article_delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Article, slug=slug)
    instance.delete()
    messages.success(request, "Successfully Deleted")

    return redirect("articles:list")




