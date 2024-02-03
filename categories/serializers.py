from django.db import IntegrityError
from rest_framework import serializers 
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = [
            'id','owner','created_at','category',
        ]