from rest_framework import serializers

from .models import Category
from subscriptions.models import Subscribe


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    subscribe_id = serializers.SerializerMethodField()

    # Add extra fields from model queryset for page statistics
    subscriptions_count = serializers.ReadOnlyField()
    product_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_subscribe_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            subscribed = Subscribe.objects.filter(
                owner=user, category=obj.id
            ).first()
            return subscribed.id if subscribed else None
        return None

    class Meta:
        model = Category
        fields = ['id', 'category', 'created_at', 'owner', 'is_owner',
                'subscribe_id', 'subscriptions_count', 'product_count']
