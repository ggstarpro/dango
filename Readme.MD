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


# [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk?hl=ja)
下記をダウンロード

```
macOS 64 ビット
(x86_64)
google-cloud-cli-473.0.0-darwin-x86_64.tar.gz	51.7 MB	9ddd90144a004d9ff630781e9b8f144c21b2cea8fb45038073b7fb82399ed478

```
ファイルを解凍し、プロジェクトにSKDを配置し書きコマンドを実施
`./google-cloud-sdk/install.sh`

```
Do you want to help improve the Google Cloud CLI (y/N)?  N
Do you want to continue (Y/n)?  Y
Enter a path to an rc file to update, or leave blank to use [/Users/gm/.bash_profile]:  Enter
Download and run Python 3.11 installer? (Y/n)? n
```

`./google-cloud-sdk/bin/gcloud init`

```
You must log in to continue. Would you like to log in (Y/n)? Y
```
Would you like to create one? (Y/n)?  Y


Enter a Project ID. Note that a Project ID CANNOT be changed later.
Project IDs must be 6-30 characters (lowercase ASCII, digits, or
hyphens) in length and start with a lowercase letter.

`{企業識別子}-{サービス識別子}-{環境識別子(3 文字 OR 4 文字)}`

# GCPプロジェクト作成
## APP Engine
asia-northeast1
IDとAPIへのアクセスはdefault

# gunicornインストールとrequirements.txtの作成
`pip install gunicorn`
`pip freeze > requirements.txt`

# GAEへデプロイ
`gcloud auth login`
`gcloud config set project $ID$`
`gcloud init`

```
$ gcloud app deploy --project $ID$
Do you want to continue (Y/n)?  Y
```

`gcloud app browse`
https://[$ID$].an.r.appspot.com/


# [CloudSQL](https://cloud.google.com/python/django/appengine?hl=ja)
- Cloud SQL Admin API, Secret Manager, and Cloud Build API を有効にする
```
次のサービスを有効にしようとしています:
Cloud SQL Admin API
Secret Manager API
Cloud Build API
```

- APIとサービス > 認証情報 > 認証情報作成 > ウィザードで選択 > Cloud SQL Admin API > ユーザデータ > 完了

## API の認証情報を取得して認証
`gcloud auth application-default login`

## ローカル環境の設定
`gcloud services enable sqladmin`

## Cloud SQL Auth Proxy をダウンロード
`curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.11.0/cloud-sql-proxy.darwin.amd64`

`chmod +x cloud-sql-proxy`

## Cloud SQL for PostgreSQL インスタンスを設定する
SQL > インスタンスを作成　> MySQL
really-site-test-instance
パスワード:
Enterprise > サンドボックス > シングルゾーン
リージョン > us-centra1 (アイオワ)
ゾーン > 任意
バージョン > MySQL 8
オプション > マシン > 1 vCPU、0.614 GB (共有コアマシン)
オプション > ストレージ > HDD > 10GB > 自動増量OFF
オプション > データ保護 > 日次バックアップの自動化OFF
オプション > データ保護 > 削除からの保護の有効化 OFF
作成

### ユーザ作成
アカウントを追加 >
ユーザ名: $username$
パスワード: $password$
ホスト名: 全てのホストを許可
追加

### データベースの作成
データベース名: really_site_test_db
文字セット: utf8
照合: デフォルトの照合

### Cloud SQL　へ接続

`./cloud-sql-proxy -instances="[$INSTANCE_CONNECTION_NAME$]=tcp:3306"`
($INSTANCE_CONNECTION_NAME$は GCPの接続名)


### mysqlclient
`brew install mysql`
`pip install mysqlclient`
`pip freeze > requirements.txt`
`./secrets/cloud-sql-proxy [$INSTANCE_CONNECTION_NAME$]`
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py createsuperuser`
`[$username$]`
`[$password$]`
```
http://127.0.0.1:8080/
(DBはGCPの方になっている)

$ gcloud app deploy --project [$ID$]
$ gcloud app browse
```

### 静的ファイルを集める(collectstatic)
`python manage.py collectstatic`