from django.db import models
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(default="", blank=False, null=False, max_length=30)
    text = models.TextField(default="")
    author = models.CharField(default="", max_length=30)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)
    created_at = models.DateField(auto_now_add=True)
    """
    他にも以下のものが存在
    OneToOne     1 : 1
    ForeignKey   1 : 多
    ManyToMany   多 : 多
    """
    # user(1) : comment(多), user削除されたらcommentは削除
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # article(1) : comment(多), user削除されたらarticleは削除
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

