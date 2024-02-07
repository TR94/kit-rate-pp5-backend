from rest_framework import generics, permissions
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from kitrate_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer

class ReviewList(generics.ListCreateAPIView):
# Django generics to create the GET and PUT methods
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.annotate(
        # FIX THIS ISSUE WITH PULLING RATING THROUGH TO REVIEW LIST
        rating=Count('product__ratings__rating', distinct=True),
    )

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['product__ratings__rating']

    def perform_create(self, serializer):
        # this associates a user with the review
        serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # Django generics takes care of GET, PUT, DELETE methods
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()