from email.policy import default
from django.db import models
from user.models import User
from file.models import File
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    images = models.ManyToManyField(File)
    is_under_reviewed = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{str(self.id)} {self.title}"


class ArticleCode(models.Model):
    code = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='codes')

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.body


class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title