from django.db.models import Count, Avg
from rest_framework import generics, filters
from kitrate_api.permissions import IsOwnerOrReadOnly

from .models import Profile
from .serializers import ProfileSerializer


# Based on Code Institute lesson material on Django REST Framework
class ProfileList(generics.ListAPIView):
    # View to list all profiles
    # Django generics takes care of GET method
    # Profile creation is handled by Django signals - profiles > models.py

    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        review_count=Count('owner__review', distinct=True),
        average_rating=Avg('owner__review__rating', distinct=True),
        subscriptions_count=Count('owner__subscriber', distinct=True),
    ).order_by('-created_at')

    filter_backends = [filters.OrderingFilter]

    ordering_fields = [
        'review_count', 'average_rating', 'subscriptions_count'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    # View to see the details of a specific profile by ID
    # Django generics takes care of GET and PUT methods

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        review_count=Count('owner__review', distinct=True),
        average_rating=Avg('owner__review__rating', distinct=True),
        subscriptions_count=Count('owner__subscriber', distinct=True),
    ).order_by('-created_at')
