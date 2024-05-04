from django.contrib import admin
from django.contrib.auth.views import LogoutView
# from django.urls import path
from django.urls import path, include
from mysite import views
from django.views.decorators.cache import cache_page

app_name = "mysite"

urlpatterns = [
    path('', views.index, name="home"),
    path('langding_mui/', views.langding_mui, name="langding_mui"),
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    # path('mypage/', views.mypage),
    path('mypage/', views.MypageView.as_view()),
    # path('contact/', views.contact),
    path('contact/', views.ContactView.as_view()),
    path('pay/', views.PayView.as_view()),
    # view単位 DBキャッシュ
    path('cache_test/', views.cache_test),
    # url単位 DBキャッシュ
    path('cache_test2/', cache_page(10)(views.cache_test2)),
    # templateキャッシュ
    path('cache_test3/', views.cache_test3),

    path('ping/', views.ping),
]
