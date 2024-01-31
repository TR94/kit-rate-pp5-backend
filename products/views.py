from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Product
from .serializers import ProductSerializer
from kitrate_api.permissions import IsOwnerOrReadOnly


# Based on Code Institute lesson material on Django REST Framework

class ProductList(APIView):
    # View to list all products

    # Setting the serializer class automatically creates a form for the "p" method
    serializer_class = ProductSerializer

    # Permissions to only allow logged in users to create a product
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Method to get products list and serialize to JSON
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

    # Method to create a new product and save it to database
    def put(self, request):
        serializer = ProductSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    # View to see the details of a specific product by ID

    # Setting the serializer class automatically creates a form for the "put" method
    serializer_class = ProductSerializer

    # Setting the permission class to allow only data owners to update their data
    permission_classes = [IsOwnerOrReadOnly]

    # Method to see if specific product is avaialble, by primary key
    def get_object(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            self.check_object_permissions(self.request, product)
            return product
        except Product.DoesNotExist:
            raise Http404

    # Method to get the specific product using get_ojbect method and serialize to JSON
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    # Method to retrieve a specific product, update details through serializer and save
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # Method to delete a specific product 
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


