from rest_framework import generics, permissions
from kitrate_api.permissions import IsOwnerOrReadOnly
from .models import Notification
from .serializers import NotificationSerializer


class NotificationList(generics.ListCreateAPIView):
    # Django generics takes care of GET and PUT methods
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_create(self, serializer):
        # this associates a user with the follow
        serializer.save(owner=self.request.user)

class NotificationDetail(generics.RetrieveDestroyAPIView):
    # Django generics takes care of GET and DELETE methods
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()