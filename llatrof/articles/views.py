from .models import Article, Category, Brand, RecommendArticle
from .serializers import ArticleListSerializer, CategoryListSerializer, BrandListSerializer, RecommendArticleListSerializer, BrandArticlesListSerializer, CategoryArticleListSerializer

from django.db.models import Q
from urllib.parse import unquote

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


#######################################
#
# by. JaeHyeon (22/1O/26)
# articles_list = Serializing Article Records
#
# args ->
# sort   = None / ascending / descending
# router = None / category / brand
# params = None / category_name / brand_name
#
#######################################
@api_view(['GET'])
def articles_list(request, sort=None, router=None, params=None):
    if sort:
        if router == 'category':
            articles = Article.objects.filter(goods_category=params)
        elif router == 'brand':
            articles = Article.objects.filter(goods_brand=params)
        if sort == 'ascending':
            articles = articles.order_by('goods_price')
        elif sort == 'descending':
            articles = articles.order_by('goods_price').reverse()
    else:
        articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)



#######################################
#
# by. JaeHyeon (22/1O/26)
# category = goods_category 를 분류하기 위한 함수
# args ->
# categorise = Article Table 내 goods_category Field 를 중복 제거한 QuerySetList
# category_list = goods_category 만 분류한 List
#
#######################################
@api_view(['GET'])
def category(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

#######################################
#
# by. JaeHyeon (22/1O/26)
# category_goods = category 기준으로 분류된 goods 만 rendering 하는 함수
# args ->
# goods_list = Article Table 내 goods_category 기준으로 variable routing 을 통해 받은 category(:str) 를 filtering 한 QuerySetList
#
#######################################
@api_view(['GET'])
def category_goods(request, category):
    goods_list = Article.objects.all().filter(goods_category=category)
    serializer = ArticleListSerializer(goods_list, many=True)
    return Response(serializer.data)

#######################################
#
# by. JaeHyeon (22/1O/26)
# brand = goods_brand 를 분류하기 위한 함수
# args ->
# brands = Article Table 내 goods_brand Friled 를 중복 제거한 QuerySetList
# brands_list = goods_brand 만 분류한 List
#
#######################################
@api_view(['GET'])
def brand(request):
    brands = Brand.objects.all()
    serialzier = BrandListSerializer(brands, many=True)
    return Response(serialzier.data)

#######################################
#
# by. JaeHyeon (22/1O/26)
# brand_goods = brand 기준으로 분류된 goods 만 rendering 하는 함수
# args ->
# goods_list = Article Table 내 goods_brand 기준으로 variable routing 을 통해 받은 brand(:str) 를 filtering 한 QuerySetList
#
#######################################
@api_view(['GET'])
def brand_goods(request, brand):
    goods_list = Article.objects.all().filter(goods_brand=brand)
    seriazlier = ArticleListSerializer(goods_list, many=True)
    return Response(seriazlier.data)

@api_view(['GET'])
def liamspick(request):
    goods_list = RecommendArticle.objects.all()
    serializer = RecommendArticleListSerializer(goods_list, many=True)
    return Response(serializer.data)

#######################################
#
# by. JaeHyeon (22/12/16)
# search_keyword = varialbe routing params 기준으로 Article records 검색
# args ->
# articles = Q 객체를 이용한 Article Object 관리
#
#######################################
@api_view(['GET'])
def search_keyword(request, search_keyword):
    search_keyword = unquote(search_keyword)
    articles = Article.objects.filter(Q(goods_title__contains=search_keyword) | Q(goods_category__category__contains=search_keyword) | Q(goods_brand__brand__contains=search_keyword))
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)