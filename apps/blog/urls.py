# Django
from django.urls import path

# Project
from .views import ArticleViewSet, ArticleCodeViewSet, CommentListAPIView, CommentCreateAPIView, ReviewListAPIView, UnReviewedArticleListAPIView

# Rest Framework
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article_code', ArticleCodeViewSet, basename='article_code')


urlpatterns = [
    path('comment/<int:pk>/', CommentListAPIView.as_view()),
    path('comment_post/<int:pk>/', CommentCreateAPIView.as_view()),
    path('review/', ReviewListAPIView.as_view()),
    path('unreviewed/', UnReviewedArticleListAPIView.as_view()),
]



urlpatterns += router.urls