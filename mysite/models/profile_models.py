from django.db import models
from django.contrib.auth import get_user_model
import os

def upload_image_to(instance, filename):
    """
    保存したとき「os.path.join('static', 'img', user_id, filename)」の場合
    static/img/{user_id}/ファイル名でファイルが保存される
    """
    user_id = str(instance.user.id)
    # return os.path.join('static', 'img', user_id, filename)

    # GCSのためstaticは別にいらないので修正
    return os.path.join('img', user_id, filename)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(default="匿名ユーザ", max_length=30)
    zipcode = models.CharField(default="", max_length=8)
    prefecture = models.CharField(default="", max_length=6)
    city = models.CharField(default="", max_length=100)
    address = models.CharField(default="", max_length=200)
    image = models.ImageField(default="", blank=True, upload_to=upload_image_to)