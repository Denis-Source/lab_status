from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from message.models import Message
from message.serializers import MessageSerializer, MessageCreateSerializer
from lab_user.models import LabUser


class MessagePagination(PageNumberPagination):
    """
    Pagination class
    sets page size of json response to 100
    """
    page_size = 100


class MessageListAPIView(ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by("-time")
    pagination_class = MessagePagination


class MessageCreateAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MessageCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=LabUser.objects.get(username=self.request.user))
