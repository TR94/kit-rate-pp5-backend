from rest_framework import serializers

from .models import Profile


# Based on from Code Institute lesson material on Django REST Framework
class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Add extra fields from model queryset for page statistics
    review_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()
    subscriptions_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'content',
            'image', 'is_owner', 'review_count', 'average_rating',
            'subscriptions_count'
        ]
