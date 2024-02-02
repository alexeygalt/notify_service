from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from client.models import Client
from client.serializers import ClientCreateSerializer, ClientUpdateSerializer
import logging

logger = logging.getLogger('app')


@extend_schema(summary="Создание нового клиента",
               description='timezone format example: Europe/Berlin')
class CreateClientView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


@extend_schema_view(
    patch=extend_schema(summary="Частичное обновление атрибутов Клиент"),
    put=extend_schema(summary="Обновление атрибутов Клиент"),
    delete=extend_schema(summary="Удалить объект Клиент"), )
class UpdateClient(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    http_method_names = ["put", "patch", "delete", ]

    def perform_destroy(self, instance):
        logger.info(f'Delete Client object-{instance.id}')
        super().perform_destroy(instance)
