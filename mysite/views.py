from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Really Site'
    }
    return render(request, 'mysite/index.html', context)