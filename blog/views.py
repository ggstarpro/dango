from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Comment
from django.core.paginator import Paginator
from blog.forms import CommentForm

def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/blogs.html', context)


def article(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            print(comment)
            comment.save()

    context = {
        'article': article,
        'comments': comments,
    }

    return render(request, 'blog/article.html', context)
