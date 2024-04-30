[toc]
# 概要
[【Python】 Django3で「本当に使える」WEBアプリケーションを開発しよう](https://www.udemy.com/course/reallysite/)を実施した

# 環境構築
$ python3 -m venv venv

$ source venv/bin/activate

$ pip install django==3.1.4
$ django-admin startproject config .
$ python manage.py startapp mysite
$ python manage.py runserver

# 便利なライブラリ
## [django-livereload](https://pypi.org/project/django-livereload/)
$ pip install django-livereload
settings.py
```
'livereload',
'django.contrib.staticfiles',
.
.
.
'django.middleware.clickjacking.XFrameOptionsMiddleware',
'livereload.middleware.LiveReloadScript',
```
$ python manage.py livereload

# ポート番号がすでに使用されていた場合
LIVERELOAD_PORT = "8080"

##
python manage.py startapp blog

## マイグレーション
$ python manage.py makemigrations
$ python manage.py migrate

## 管理者作成
python manage.py createsuperuser
Email: test@example.com
Password: p@ssword

# Bootstrap Icons
https://icons.getbootstrap.com/

# ライブラリ
pip install PyYAML