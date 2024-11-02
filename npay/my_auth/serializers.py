from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Extra fields for profile information
    phone_number = serializers.CharField(required=False, write_only=True)
    address = serializers.CharField(required=False, write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "phone_number", "address"]

    def create(self, validated_data):
        # Extract profile fields
        phone_number = validated_data.pop("phone_number", None)
        address = validated_data.pop("address", None)

        # Create the user
        user = User(username=validated_data["username"], email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()

        # Create associated UserProfile if additional data exists
        UserProfile.objects.create(
            user=user, phone_number=phone_number, address=address
        )

        return user
