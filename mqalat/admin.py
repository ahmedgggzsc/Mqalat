from django.contrib import admin
from .models import Article, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published', 'featured', 'views_count')
    list_filter = ('category', 'is_published', 'featured')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
