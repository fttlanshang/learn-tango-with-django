from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):
    context_dict = {}
    # retrieve top 5 categories ordered by likes
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict['categories'] = category_list
    # retrieve top 5 pages ordered by views
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', context=None)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context=context_dict)