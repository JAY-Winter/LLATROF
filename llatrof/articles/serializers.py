from rest_framework import serializers
from .models import Article, Category, Brand, RecommendArticle


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

class RecommendArticleListSerializer(serializers.ModelSerializer):
    goods = ArticleListSerializer()
    
    class Meta:
        model = RecommendArticle
        fields = '__all__'