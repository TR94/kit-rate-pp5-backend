from rest_framework import serializers 
from .models import Notification
from products.serializers import ProductSerializer


class NotificationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Notification
        fields = [
            'id','owner','target','content','created_at','product_title',
        ]