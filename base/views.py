from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    data = {}
    data['data'] = 'BOOKS'
    return render(request, 'base/index.html', data)