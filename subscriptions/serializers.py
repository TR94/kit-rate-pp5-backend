from django.db import IntegrityError
from rest_framework import serializers 
from .models import Subscribe
from categories.serializers import CategorySerializer


class SubscribeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Subscribe
        fields = [
            'id','owner','created_at','category_detail',
        ]

    # to handle a user subscribing to the same category twice 
    def create(self, validated_data):
        try: 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':'cannot subscribe to the same category twice'
            })