from rest_framework import serializers
from profiles_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    def create(self, validated_data) -> models.UserProfile:
        """Сreate and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user profile"""

        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)

    class Meta:
        model = models.UserProfile
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializers profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ['id', 'user_profile', 'status_text', 'created_on']
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }