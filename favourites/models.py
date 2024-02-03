from django.db import models
from django.contrib.auth.models import User 
from products.models import Product 


# Favourite model based on the DRF walkthough project from Code Institute
class Favourites(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favourites')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # User can only favourite a product once
        unique_together = ['owner', 'product']

    def __str__(self):
        return f'{self.owner} {self.product}'