from django.db import models

# Create your models here.
class  Article(models.Model):
    title = models.CharField(default="", blank=False, null=False, max_length=30)
    text = models.TextField(default="")
    author = models.CharField(default="", max_length=30)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
