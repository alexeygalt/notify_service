from rest_framework import serializers
from message.models import Message


class MessageBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
