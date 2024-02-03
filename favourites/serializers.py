from django.db import IntegrityError
from rest_framework import serializers 
from .models import Favourites


class FavouriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favourites
        fields = [
            'id','owner','created_at','product',
        ]

    # to handle a user favouriting the same product twice 
    def create(self, validated_data):
        try: 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':'cannot favourite the same product twice'
            })