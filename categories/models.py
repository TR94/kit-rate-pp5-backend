from django.db import models
from django.contrib.auth.models import User


# Category model based on the DRF walkthough project from Code Institute
class Category(models.Model):

    # List of product categories, allows users to follow categories
    product_categories = [
        ('accessories', 'Accessories'),
        ('bikes', 'Bikes'),
        ('components', 'Components'),
        ('clothing', 'Clothing'),
        ('health and fitness', 'Health and Fitness'),
        ('tools and workshop', 'Tools and Workshop'),
    ]

    category = models.CharField(max_length=32, choices=product_categories, default="Accessories")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.category}'