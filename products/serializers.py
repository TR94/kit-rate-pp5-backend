from rest_framework import serializers
from .models import Product

# Taken from Code Institute lesson material on Django REST Framework

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # Add extra field for conditional rendering, such as edit/delete buttons which are user specific
    is_owner = serializers.SerializerMethodField()

    # Add extra fields for profile related data
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # built in rest framework validation uses "validate_[field name]"
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            #2MB file size limit 
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    # Method to check user is the same as the object's owner
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Product
        fields = [
            # note: 'id' is added automatically in the Product model and must be included in the serializer
            'id', 'owner', 'created_at', 'updated_at', 'title', 'description',
            'image','category', 'is_owner', 'profile_id', 'profile_image',
        ]