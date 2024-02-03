from rest_framework import generics, permissions
from kitrate_api.permissions import IsOwnerOrReadOnly
from ratings.models import Ratings
from ratings.serializers import RatingSerializer


class RatingList(generics.ListCreateAPIView):
    # Django generics takes care of GET method
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ratings.objects.all()

    def perform_create(self, serializer):
        # this associates a user with the like
        serializer.save(owner=self.request.user)

class RatingDetail(generics.RetrieveDestroyAPIView):
    # Django generics takes care of GET and DELETE methods
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Ratings.objects.all()