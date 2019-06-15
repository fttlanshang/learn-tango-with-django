from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {"boldmessage": "A lovely dog!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', context=None)
