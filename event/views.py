from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from event.serializers import EventSerializer, EventCreateSerializer, EventAddVideoSerializer
from event.models import Event


class EventPagination(PageNumberPagination):
    """
    Pagination class
    sets page size of json response to 100
    """
    page_size = 100


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    pagination_class = EventPagination
    queryset = Event.objects.all().order_by("-time")


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]  # TODO
    permission_classes = [IsAuthenticated]


class EventAddVideoAPIView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventAddVideoSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]  # TODO
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.validated_data["is_video_recorded"] = True
        serializer.save()
