from rest_framework import generics, permissions
from kitrate_api.permissions import IsOwnerOrReadOnly
from favourites.models import Favourites
from favourites.serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    # Django generics takes care of GET and PUT method
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favourites.objects.all()

    def perform_create(self, serializer):
        # this associates a user with the like
        serializer.save(owner=self.request.user)

class FavouriteDetail(generics.RetrieveDestroyAPIView):
    # Django generics takes care of GET and DELETE methods
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourites.objects.all()