from rest_framework.generics import ListAPIView

from message.models import Message
from message.serializers import MessageSerializer


class MessageListAPIView(ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by("-time")
