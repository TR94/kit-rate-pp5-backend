from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # Add extra field for conditional rendering, such as edit/delete buttons which are user specific
    is_owner = serializers.SerializerMethodField()

    # Add extra fields for profile related data
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # Add extra field as read ony from queryset annotation 
    rating = serializers.ReadOnlyField()

    # Method to check user is the same as the object's owner
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Review
        fields = [
            # note: 'id' is added automatically in the Review model and must be included in the serializer
            'id', 'owner','product', 'created_at', 'updated_at', 
            'content', 'is_owner', 'profile_id', 'profile_image', 'rating',
        ]

# Serializer to ensure the review is always associated with the same product
class ReviewDetailSerializer(ReviewSerializer):
    product = serializers.ReadOnlyField(source='product.id')