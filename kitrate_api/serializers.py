from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

# Code taken from dj-rest-auth documentation
class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_username = serializers.ReadOnlyField(source='user.username')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id','profile_username', 'profile_image'
        )