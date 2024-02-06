from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from kitrate_api.permissions import IsOwnerOrReadOnly


# Based on Code Institute lesson material on Django REST Framework

class ProfileList(generics.ListAPIView):
    # View to list all profiles
    # Django generics takes care of GET method
    # Profile creation is handled by Django signals - profiles > models.py

    # Setting the serializer class automatically creates a form for the "put" method
    serializer_class = ProfileSerializer

    queryset = Profile.objects.all()

class ProfileDetail(generics.RetrieveUpdateAPIView):
    # View to see the details of a specific profile by ID
    # Django generics takes care of GET and PUT methods

    # Setting the serializer class automatically creates a form for the "put" method
    serializer_class = ProfileSerializer

    # Setting the permission class to allow only data owners to update their data
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.all()



