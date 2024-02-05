from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from core.models import User

USER_MODEL = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = USER_MODEL
        fields = (
            "id",
            "email",
            "password",
            "password_repeat",
        )
        extra_kwargs = {"password_repeat": {"write_only": True}}

    def validate_password(self, data):
        validate_password(data)
        return data

    def validate_password_repeat(self, data):
        if data != self.initial_data.get("password"):
            raise serializers.ValidationError("Passwords are not the same")
        return data

    def create(self, validated_data):
        validated_data.pop("password_repeat")
        email = validated_data.pop("email").lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Not unique email")
        user = USER_MODEL.objects.create_user(email=email, **validated_data)
        user.save()
        return user


class UserBase(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "auth_provider",
            "last_login",
            "date_joined",
            "is_active",
        )
