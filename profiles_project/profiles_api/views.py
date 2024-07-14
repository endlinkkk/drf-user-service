from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from profiles_api import serializers, models, permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.UpdateOwnProfile,]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name', 'email',]


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    