from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from core.models import User
from core.serializers import UserRegistrationSerializer, UserBase


@extend_schema(
    summary="Регистрация нового пользователя",
)
class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


@extend_schema(
    summary="Получение информации о текущем пользователе",
)
class GetMe(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserBase
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
