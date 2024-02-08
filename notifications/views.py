from rest_framework import generics, permissions
from kitrate_api.permissions import IsOwnerOrReadOnly
from .models import Notification
from .serializers import NotificationSerializer


class NotificationList(generics.ListCreateAPIView):
# Django generics takes care of GET and PUT methods
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Notification.objects.all()

class NotificationDetail(generics.RetrieveDestroyAPIView):
    # Django generics takes care of GET and DELETE methods
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()