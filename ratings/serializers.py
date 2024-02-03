from django.db import IntegrityError
from rest_framework import serializers 
from .models import Ratings


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ratings
        fields = [
            'id','owner','created_at','product', 'rating',  
        ]

    # to handle a user rating the same product twice 
    def create(self, validated_data):
        try: 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':'possible duplicate'
            })