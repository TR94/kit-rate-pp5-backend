from django.db import models
from django.contrib.auth.models import User
from products.models import Product 
from categories.models import Category


# Subscribe model based on the DRF walkthough project from Code Institute
# Owner subscribes to a category from the product model and returns all products related to that category
class Subscribe(models.Model):
   
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subscribed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.subscribed}'