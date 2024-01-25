from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Product
from .serializers import ProductSerializer


# Taken from Code Institute lesson material on Django REST Framework
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
