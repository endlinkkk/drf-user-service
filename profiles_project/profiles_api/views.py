from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status, viewsets
from profiles_api import serializers, models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
