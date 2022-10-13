from django.contrib import admin
from .models import Article, ArticleCode, Comment, Review

# Register your models here.
class ArticleCodeLine(admin.StackedInline):
    model = ArticleCode
    extra = 1


class ReviewLine(admin.StackedInline):
    model = Review
    extra = 1


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [ArticleCodeLine, ReviewLine]


admin.site.register(Comment)


admin.site.register(Review)