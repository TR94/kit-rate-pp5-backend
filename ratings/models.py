from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product

# Ratings model based on the DRF walkthough project from Code Institute
class Ratings(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # User can only leave one rating per product to stop them skewing the overall product rating
        unique_together = ['owner', 'product']

    def __str__(self):
        return f'{self.owner} {self.product} {self.rating}'