from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Comment, Tag
from django.core.paginator import Paginator
from blog.forms import CommentForm

def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
        'page_title': 'ブログ一覧',
    }
    return render(request, 'blog/blogs.html', context)

def article(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        if request.POST.get('like_count', None):
            article.count += 1
            article.save()
        else:
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

def tags(request, slug):
    tag = Tag.objects.get(slug=slug)
    articles = tag.article_set.all()
    print('_set>>')
    print(articles)

    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
        'page_title': '記事一覧  #{}'.format(slug),
    }

    return render(request, 'blog/blogs.html', context)


from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@ensure_csrf_cookie
def like(request, pk):
    d = {"message": "error"}
    if request.method == 'POST':
        print("post")
        obj = Article.objects.get(pk=pk)
        obj.count += 1
        obj.save()

        d["message"] = "success"
    return JsonResponse(d)