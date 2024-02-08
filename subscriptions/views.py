from rest_framework import generics, permissions
from kitrate_api.permissions import IsOwnerOrReadOnly
from .models import Subscribe
from .serializers import SubscribeSerializer


class SubscribeList(generics.ListCreateAPIView):
# Django generics takes care of GET and PUT methods
    serializer_class = SubscribeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subscribe.objects.all()


    def perform_create(self, serializer):
        # this associates a user with the follow
        serializer.save(owner=self.request.user)

class SubscribeDetail(generics.RetrieveDestroyAPIView):
    # Django generics takes care of GET and DELETE methods
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()