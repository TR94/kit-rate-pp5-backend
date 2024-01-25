from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Product
from .serializers import ProductSerializer


# Taken from Code Institute lesson material on Django REST Framework
class ProductList(APIView):
    # View to list all products

    # Method to get products list and serialize to JSON
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

