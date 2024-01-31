from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Profile
from .serializers import ProfileSerializer
from kitrate_api.permissions import IsOwnerOrReadOnly


# Based on Code Institute lesson material on Django REST Framework

class ProfileList(APIView):
    # View to list all profiles
    # Profile creation is handled by Django signals - profiles > models.py

    # Method to get profiles list and serialize to JSON
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDetail(APIView):
    # View to see the details of a specific profile by ID

    # Setting the serializer class automatically creates a form for the "put" method
    serializer_class = ProfileSerializer

    # Setting the permission class to allow only data owners to update their data
    permission_classes = [IsOwnerOrReadOnly]

    # Method to see if specific profile is avaialble, by primary key
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    # Method to get the specific profile using get_ojbect method and serialize to JSON
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    # Method to retrieve a specific profile, update details through serializer and save
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


