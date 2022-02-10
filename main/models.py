from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='pics/categories', null = True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('category_slug', args=[self.slug])

        
    def __str__(self):
        return self.category_name
