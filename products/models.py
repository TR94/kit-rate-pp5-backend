from django.db import models
from django.contrib.auth.models import User


# Product model based on the DRF walkthough project from Code Institute
class Product(models.Model):

    # List of product categories, allows users to follow categories
    product_categories = [
        ('accessories', 'Accessories'),
        ('bikes', 'Bikes'),
        ('components', 'Components'),
        ('clothing', 'Clothing'),
        ('health and fitness', 'Health and Fitness'),
        ('tools and workshop', 'Tools and Workshop'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default="../default_post_tt7esj", blank=True
    )
    category = models.CharField(max_length=32, choices=product_categories, default="Accessories")
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id}, {self.title}'