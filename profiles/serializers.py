from rest_framework import serializers
from .models import Profile

# Taken from Code Institute lesson material on Django REST Framework

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # Add extra fields from model queryset for page statistics
    review_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()
    subscriptions_count = serializers.ReadOnlyField()

    # Add extra field for conditional rendering, such as edit/delete buttons which are user specific
    is_owner = serializers.SerializerMethodField()

    # Method to check user is the same as the object's owner
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            # note: 'id' is added automatically in the Profile model and must be included in the serializer
            'id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'image', 
            'is_owner', 'review_count', 'average_rating', 'subscriptions_count',
        ]