from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = "Hello rango, bro! Welcome page <a href='/rango/about'> ABOUT </a>"
    return HttpResponse(html)


def about(request):
    html = "This is the about page. Come back to <a href='/rango/'> Index </a>"
    return HttpResponse(html)