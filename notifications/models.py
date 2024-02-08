from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Notification(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target")
    content = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    product_title = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product_title")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner} notifying {self.target}"
    