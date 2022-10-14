# Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics

# Project
from .serializers import ArticleSerializer, ArticlePostSerializer, ArticleCodeSerializer, CommentListSerializer, CommentCreateSerializer, ReviewSerializer
from .models import Article, ArticleCode, Review
from .permissions import IsAuthorOrReadOnly
from user.models import User

# Django
from django.shortcuts import get_object_or_404


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        return Article.objects.filter(is_reviewed=True) 
    
    def perform_create(self, serializer):
        author = get_object_or_404(User, id=self.request.user.id)
        serializer.save(author = author)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleSerializer
        return ArticlePostSerializer


class UnReviewedArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(is_reviewed=False)


class ArticleCodeViewSet(ModelViewSet):
    queryset = ArticleCode.objects.all()
    serializer_class = ArticleCodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    
    def get_queryset(self):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        return article.comment_set.all()


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        user = self.request.user
        return serializer.save(article=article, user=user)


class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        Review.objects.filter(article__is_reviewed=True).delete()
        return Review.objects.filter(article__author=self.request.user)