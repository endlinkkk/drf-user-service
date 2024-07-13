from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from profiles_api import serializers, models, permissions
from rest_framework import filters


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.UpdateOwnProfile,]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name', 'email',]