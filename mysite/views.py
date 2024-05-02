from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail
import os

def index(request: HttpRequest) -> HttpResponse:
    ranks = Article.objects.order_by('-count')[:2] # 降順
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Really Site',
        'articles': articles,
        'ranks': ranks
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
            # ログインさせる
            login(request, user)
            messages.success(request, '登録完了')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)

@login_required
def mypage(request):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '更新完了しました')
    return render(request, 'mysite/mypage.html', context)

def contact(request):
    context = {
        'grecaptcha_sitekey': os.environ['GRECAPTCHA_SITEKEY']
    }
    if request.method == 'POST':
        recaptcha_token = request.POST.get('g-recaptcha-response')
        response = grecaptcha_request(recaptcha_token)
        if not response:
            messages.error(request, 'reCAPTCHAに失敗しました')
            return redirect(request, 'mysite/contact.html', context)
        subject = 'お問い合わせがありました'
        message = """お問い合わせがありました\n名前: {}\nメールアドレス: {}\n内容: {}""".format(
            request.POST.get('name'),
            request.POST.get('email'),
            request.POST.get('content'),
        )
        from_email = os.environ['DEFAULT_EMAIL_FROM']
        recipient_list = [
            os.environ['DEFAULT_EMAIL_FROM']
        ]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list
        )
        messages.success(request, 'お問い合わせしました')
    return render(request, 'mysite/contact.html', context)


def grecaptcha_request(token):
    from urllib import request, parse
    import json, ssl

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

    url = "https://www.google.com/recaptcha/api/siteverify"
    headers = { 'content-type': 'application/x-www-form-urlencoded' }
    data = {
        'secret': os.environ['GRECAPTCHA_SECRETKEY'],
        'response': token,
    }
    data = parse.urlencode(data).encode()
    req = request.Request(
        url,
        method="POST",
        headers=headers,
        data=data,
    )
    f = request.urlopen(req, context=context)
    response = json.loads(f.read())
    f.close()

    print('grecaptcha_request response')
    print(response)
    return response['success']

