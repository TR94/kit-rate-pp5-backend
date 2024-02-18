from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


# Product model based on the DRF walkthough project from Code Institute
class Product(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default="../default_post_tt7esj", blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.title}'