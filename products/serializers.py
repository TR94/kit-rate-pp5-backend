from rest_framework import serializers
from .models import Product
from categories.models import Category
from favourites.models import Favourites
from categoriges.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_detail = CategorySerializer(source='category', read_only=True)
    

    # Add extra field for conditional rendering, such as edit/delete buttons which are user specific
    is_owner = serializers.SerializerMethodField()

    # Add extra fields for profile related data
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # Add extra field to track favourite products
    favourite_id = serializers.SerializerMethodField()

    # Add extra fields from model queryset for page statistics
    review_count = serializers.ReadOnlyField()
    favourited_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()

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

    # Method to check if the user have favourited a specific product or not
    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourited = Favourites.objects.filter(
                owner=user, product=obj
            ).first()
            return favourited.id if favourited else None
        return None


    class Meta:
        model = Product
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'description', 'image', 'category', 'is_owner',
            'profile_id', 'profile_image', 'favourite_id','review_count', 'favourited_count', 'average_rating',
        ]