from django.db.models import Count
from rest_framework import generics, permissions, filters
from kitrate_api.permissions import IsOwnerOrReadOnly
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
# Django generics takes care of GET and PUT methods
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.annotate(
        subscriptions_count=Count('subscribed', distinct=True),
        product_count=Count('product', distinct=True),
    )
    filter_backends = [filters.OrderingFilter]

    ordering_fields = [
        'subscriptions_count', 'product_count'
    ]

class CategoryDetail(generics.RetrieveDestroyAPIView):
# Django generics takes care of GET and DELETE methods
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.annotate(
        subscriptions_count=Count('subscribed', distinct=True),
        product_count=Count('product', distinct=True),
    )
    filter_backends = [filters.OrderingFilter]

    ordering_fields = [
        'subscriptions_count', 'product_count'
    ]