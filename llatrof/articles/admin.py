from django.contrib import admin
from .models import Article, Category, Brand, RecommendArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(RecommendArticle)

