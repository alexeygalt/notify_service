from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from core.social_auth.serializers import (
    GoogleSocialAuthSerializer,
    FacebookSocialAuthSerializer,
)


@extend_schema(
    summary="Авторизация с помощью Google",
)
class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST  "auth_token"

        Отправьте id_token от Google, чтобы получить информацию о пользователе.

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data)["auth_token"]
        return Response(data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Авторизация с помощью Facebook",
)
class FacebookSocialAuthView(GenericAPIView):
    serializer_class = FacebookSocialAuthSerializer

    def post(self, request):
        """

        POST c "auth_token"

        Отправьте токен доступа от Facebook, чтобы получить информацию о пользователе.

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data["auth_token"]
        return Response(data, status=status.HTTP_200_OK)
