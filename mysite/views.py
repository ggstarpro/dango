from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm
from django.contrib import messages

def index(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Really Site',
        'articles': articles,
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name='mysite/auth.html'

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        messages.success(self.request, 'ログイン完了')
        return super().form_valid(form)
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.success(self.request, 'ログインエラー')
        return super().form_invalid(form)

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            messages.success(request, '登録完了')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)
