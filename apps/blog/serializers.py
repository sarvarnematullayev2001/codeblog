# Rest Framework
from rest_framework import serializers

# Project
from .models import Article, ArticleCode, Comment, Review
from file.serializers import FileSerializer
from user.serializers import UserSerializer


class ArticleCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArticleCode
        fields = '__all__'
        read_only_fields = ['article']


class ArticleSerializer(serializers.ModelSerializer):
    codes = ArticleCodeSerializer(read_only=True, many=True)
    
    class Meta:
        model = Article
        fields= ['url', 'id', 'title', 'body', 'codes', 'author', 'created_datetime', 
                'updated_datetime', 'tags', 'images', 'is_reviewed', 'is_under_reviewed']
    
    def to_representation(self, instance):
        self.fields['images'] = FileSerializer(many=True, context=self.context)
        self.fields['author'] = UserSerializer()
        return super(ArticleSerializer, self).to_representation(instance)


class ArticlePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields= ['title', 'body', 'tags', 'images']
    
    def to_representation(self, instance):
        self.fields['images'] = FileSerializer(many=True, context=self.context)
        return super(ArticlePostSerializer, self).to_representation(instance)


class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        exclude = ['user', 'article', 'active']


class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['user'] = UserSerializer()
        self.fields['article'] = ArticleSerializer()
        return super(CommentListSerializer, self).to_representation(instance)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'title', 'body', 'created_datetime', 'article']
    
    def to_representation(self, instance):
        self.fields['article'] = ArticleSerializer()
        return super().to_representation(instance)