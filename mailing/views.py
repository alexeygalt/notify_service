from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
    OpenApiParameter,
)
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from mailing.filters import MailingActiveFilter
from mailing.models import Mailing
from mailing.serializers import (
    CreateMailingSerializer,
    MailingBaseSerializer,
    MailingListSerializer,
    UpdateMailingSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
import logging

logger = logging.getLogger("app")


@extend_schema(
    description="client_filter JSON object with possible keys: operator_code, tag. time_interval : HH:mm-HH:mm",
    summary="Создание новой рассылки",
)
class CreateMailingView(CreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = CreateMailingSerializer


@extend_schema_view(
    patch=extend_schema(summary="Частичное обновление атрибутов Рассылки"),
    put=extend_schema(summary="Обновление атрибутов Рассылки"),
    delete=extend_schema(summary="Удалить объект Рассылка"),
)
class UpdateMailing(RetrieveUpdateDestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = UpdateMailingSerializer
    http_method_names = [
        "put",
        "patch",
        "delete",
    ]

    def perform_destroy(self, instance):
        logger.info(f"Delete Mailing object-{instance.id}")
        super().perform_destroy(instance)


@extend_schema(
    summary="Общая статистика по созданным рассылкам",
)
class MailingListView(ListAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingListSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = MailingActiveFilter
