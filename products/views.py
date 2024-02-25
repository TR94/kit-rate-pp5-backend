from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from kitrate_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer


# Based on Code Institute lesson material on Django REST Framework
class ProductList(generics.ListCreateAPIView):
    # View to list all products
    # Django generics takes care of GET and PUT methods

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.annotate(
        favourited_count=Count('favourites', distinct=True),
        review_count=Count('review', distinct=True),
        average_rating=Avg('review__rating', distinct=True),
    )

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__username',
        'category',
        'review__rating',
        'category__subscribed__owner',
        'favourites__owner',
        'favourites__created_at',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'favourited_count', 'average_rating', 'review_count'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # View to see the details of a specific product by ID
    # Django generics takes care of GET, PUT and DELETE methods

    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.annotate(
        favourited_count=Count('favourites', distinct=True),
        review_count=Count('review', distinct=True),
        average_rating=Avg('review__rating', distinct=True),
    )
