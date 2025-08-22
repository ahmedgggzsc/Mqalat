from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
