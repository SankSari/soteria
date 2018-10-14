from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('Page being built')
