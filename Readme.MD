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

# reCAPTCHA
v3 Admin Console
ラベル > ReallySite
チャレンジv2 > 私はロボットで貼りません
ドメイン > localhost
ドメイン > mg-test-django3-dev.an.r.appspot.com  (https://mg-test-django3-dev.an.r.appspot.com)

```
# google reCAPTCHA の　開発用キーになります。
# 参考: https://developers.google.com/recaptcha/docs/faq#im-getting-an-error-localhost-is-not-in-the-list-of-supported-domains-this-was-working-before-what-should-i-do
```

## 設定
https://developers.google.com/recaptcha/docs/display?hl=ja

# migrationファイルupload_to
設定すると下記エラーが出るので`pip install Pillow`

```
SystemCheckError: System check identified some issues:
ERRORS:
mysite.Profile.img: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```

# GCS
*
APIとサービス > 認証情報 > 編集 > キーを追加 > JSON > 作成
jsonファイルをsecretsフォルダ配下に配置

*
Storage > バケットを作成 > gg-really-site > Region > asia-northeast1 > Standard > きめ細かい管理 > 削除ボリシーOFF > 作成
```
公開アクセスの防止
このバケットは、公共のインターネット上でバケット内のデータが公開されないように設定されています。
公開アクセスを必要とするユースケース（静的ウェブサイトのホスティングなど）がある場合を除き、この設定は有効のままにしてください。この設定は今すぐでも後からでも変更可能です。
▫︎このバケットに対する公開アクセス禁止を適用する
```
*
`pip install django-storages`
`pip install google-cloud-storage`

*誰でも見れるように
新しいプリンシパル > allUsers
ロール > Storage > Storageオブジェクト閲覧者

# 決済 [PAY.JP](https://pay.jp/)
`pip install payjp`

* https://pay.jp/docs/api/?python#
* https://pay.jp/docs/flask-checkout



## 支払い処理を試してみましょう。
```
項目	        値
カード番号	4242424242424242
有効期限	12/26
CVC	       123
カード名義	PAY TARO
```

# [Google アナリティクス](https://analytics.google.com/analytics/web/?hl=ja&pli=1#)
アカウントの詳細 > アカウント名 > ReallySite
▫︎ Google のプロダクトとサービス
▫︎ モデリングのためのデータ提供とビジネス分析情報
▫︎ テクニカル サポート
▫︎ ビジネスの最適化案

プロパティ名（必須）> really-site
タイムゾーン > 日本
通貨 > ドル
その他　>　小規模

プラットフォームを選択してください > Web > mg-test-django3-dev.an.r.appspot.com > ReallySite (ストリーム名)

グローバルサイトタグ
```
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q6XWT1WFL0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-Q6XWT1WFL0');
</script>
```
- pip freeze > requirements.txt
- python manage.py collectstatic

```
You have requested to collect static files at the destination
location as specified in your settings:
    django3/staticfiles
This will overwrite existing files!
Are you sure you want to do this?
Type 'yes' to continue, or 'no' to cancel: yes
```

gcloud app deploy --project mg-test-django3-dev

# [Googleサーチコンソールの設定](https://search.google.com/search-console/about?hl=ja)
URLプレフィックス: https://mg-test-django3-dev.an.r.appspot.com


# [Google AdSense](https://adsense.google.com/intl/ja_jp/start/)
申請しないとできないので今回はしない。


