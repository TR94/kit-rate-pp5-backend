from rest_framework import generics, permissions
from kitrate_api.permissions import IsOwnerOrReadOnly

from .models import Subscribe
from .serializers import SubscribeSerializer


class SubscribeList(generics.ListCreateAPIView):
    # View to list all subscriptions
    # Django generics takes care of GET and PUT methods

    serializer_class = SubscribeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subscribe.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubscribeDetail(generics.RetrieveDestroyAPIView):
    # View to see details of a specific subscription by ID
    # Django generics takes care of GET and DELETE methods
    
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

    def delete(self, request, pk, *args, **kwargs):
        # user = User.objects.get(id=request.user.id)

        subscription = Subscribe.objects.filter(category=pk, owner=self.request.user).first()
        
        if subscription:
            subscription.delete()


class MySubscriptions(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        return Subscribe.objects.filter(owner=self.request.user)
