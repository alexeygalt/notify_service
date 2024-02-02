from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from main.settings import env
from core.services.user_dao import UserDAO
from .services import Google, Facebook


class GoogleSocialAuthSerializer(serializers.Serializer):
    """Обрабатывает сериализацию данных, связанных с Google."""

    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = Google.validate(auth_token)
        try:
            user_data["sub"]
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )

        if user_data["aud"] != env.str("GOOGLE_OAUTH2_KEY"):
            raise AuthenticationFailed("oops, who are you?")

        email = user_data["email"]
        provider = "google"

        return UserDAO.register_social_user(provider=provider, email=email)


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Обрабатывает сериализацию данных, связанных с Facebook."""

    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = Facebook.validate(auth_token)
        email = user_data["email"]
        provider = "facebook"
        return UserDAO.register_social_user(provider=provider, email=email)
