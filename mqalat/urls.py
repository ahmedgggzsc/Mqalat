from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/<slug:slug>/', views.category_articles, name='category_articles'),
    path('search/', views.search_articles, name='search_articles'),
    path('about/', views.about, name='about'),
]
