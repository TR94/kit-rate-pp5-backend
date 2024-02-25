from django.db.models import Count
from rest_framework import generics, permissions, filters
from kitrate_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    # View to list all categories
    # Django generics takes care of GET and PUT methods

    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.annotate(
        subscriptions_count=Count('subscribed', distinct=True),
        product_count=Count('product', distinct=True),
    )

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'category',
        'product__review__rating',
    ]

    search_fields = [
        'product__title',
    ]

    ordering_fields = [
        'subscriptions_count', 'product_count'
    ]


class CategoryDetail(generics.RetrieveDestroyAPIView):
    # View to see the details of a specific category by ID
    # Django generics takes care of GET and DELETE methods

    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.annotate(
        subscriptions_count=Count('subscribed', distinct=True),
        product_count=Count('product', distinct=True),
    )
