from rest_framework import serializers
from .models import Article, Category, Brand


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