from rest_framework import serializers 
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Notification
        fields = [
            'id','owner','target','content','created_at','product_title',
        ]