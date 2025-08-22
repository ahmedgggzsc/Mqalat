from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator

def home(request):
    articles_list = Article.objects.filter(is_published=True).order_by('-featured','-created_at')
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    categories = Category.objects.all()
    featured_articles = Article.objects.filter(featured=True)[:3]
    return render(request, 'mqalat/home.html', {'articles': articles, 'categories': categories, 'featured_articles': featured_articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_published=True)
    article.views_count +=1
    article.save()
    categories = Category.objects.all()
    return render(request, 'mqalat/article_detail.html', {'article': article, 'categories': categories})

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles_list = Article.objects.filter(category=category, is_published=True)
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'mqalat/category.html', {'articles': articles, 'category': category, 'categories': categories})

def search_articles(request):
    query = request.GET.get('q')
    articles_list = Article.objects.filter(title__icontains=query, is_published=True) if query else Article.objects.none()
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'mqalat/search_results.html', {'articles': articles, 'query': query, 'categories': categories})

def about(request):
    categories = Category.objects.all()
    return render(request, 'mqalat/about.html', {'categories': categories})
