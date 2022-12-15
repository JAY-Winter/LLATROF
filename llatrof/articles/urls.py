from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list),
    path('<int:article_id>', views.article),
    path('<str:sort>/<str:router>/<str:params>', views.articles_list),
    path('category', views.category),
    path('category/<str:category>', views.category_goods),
    path('brand', views.brand),
    path('brand/<str:brand>', views.brand_goods),
    path('liamspick', views.liamspick),
    path('search/<str:search_keyword>',views.search_keyword),
]