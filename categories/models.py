from django.db import models
from django.contrib.auth.models import User


# Category model based on the DRF walkthough project from Code Institute
class Category(models.Model):

    category = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return f'{self.category}'