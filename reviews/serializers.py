from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Add extra fields for profile related data
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # Add these fields to display how long ago a review was made
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    # Method to check user is the same as the object's owner
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Methods to display how long ago a review was made
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'product', 'created_at', 'updated_at',
            'content', 'rating', 'is_owner', 'profile_id', 'profile_image',
        ]


# Serializer to ensure the review is always associated with the same product
class ReviewDetailSerializer(ReviewSerializer):
    product = serializers.ReadOnlyField(source='product.id')
