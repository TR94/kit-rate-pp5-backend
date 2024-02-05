from rest_framework import generics, permissions
from kitrate_api.permissions import IsOwnerOrReadOnly
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
# Django generics takes care of GET and PUT methods
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()

class CategoryDetail(generics.RetrieveDestroyAPIView):
# Django generics takes care of GET and DELETE methods
    serializer_class = CategorySerializer
    queryset = Category.objects.all()