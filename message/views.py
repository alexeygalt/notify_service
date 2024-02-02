from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from message.models import Message
from message.serializers import MessageBaseSerializer


@extend_schema(
    summary="Получение детальной статистики отправленных сообщений по конкретной рассылке",
)
class SentMessagesByMailingList(ListAPIView):
    serializer_class = MessageBaseSerializer

    def get_queryset(self):
        return Message.objects.filter(
            mailing_id=self.kwargs["pk"],
            send_status=Message.MessageStatus.SENT,
        )
