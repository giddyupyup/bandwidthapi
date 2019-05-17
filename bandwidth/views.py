from django.http import HttpResponse
from django.shortcuts import render


def simple_view(request):
    html = '<h1>Hello World</h1>'
    return HttpResponse(html)
