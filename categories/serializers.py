from rest_framework import serializers 
from .models import Category
from subscriptions.models import Subscribe


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    subscribe_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # not sure about this at the momment - think the filter set is incorrect, confusing as Im using numerical id's for everything
    def get_subscribe_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            subscribed = Subscribe.objects.filter(
                owner=user, category=obj.id
            ).first()
            return user.username if subscribed else None
        return None

    class Meta:
        model = Category
        fields = ['id', 'category', 'created_at', 'owner', 'is_owner', 'subscribe_id']