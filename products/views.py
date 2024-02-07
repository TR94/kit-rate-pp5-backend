from django.db.models import Count, Avg
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from kitrate_api.permissions import IsOwnerOrReadOnly


# Based on Code Institute lesson material on Django REST Framework

class ProductList(generics.ListCreateAPIView):
    # View to list all products
    # Django generics takes care of GET and PUT methods
    
    # Setting the serializer class automatically creates a form for the "put" method
    serializer_class = ProductSerializer

    # Permissions to only allow logged in users to create a product
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Product.objects.annotate(
        favourited_count=Count('favourites', distinct=True),
        review_count=Count('review', distinct=True),
        average_rating=Avg('ratings__rating', distinct=True),
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # View to see the details of a specific product by ID
    # Django generics takes care of GET, PUT and DELETE methods

    # Setting the serializer class automatically creates a form for the "put" method
    serializer_class = ProductSerializer

    # Setting the permission class to allow only data owners to update their data
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Product.objects.annotate(
        favourited_count=Count('favourites', distinct=True),
        review_count=Count('review', distinct=True),
        average_rating=Avg('ratings__rating', distinct=True),
    )



