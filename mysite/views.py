from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from blog.models import Article

def index(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Really Site',
        'articles': articles,
    }
    return render(request, 'mysite/index.html', context)