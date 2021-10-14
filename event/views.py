from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from event.serializers import EventSerializer
from event.models import Event


class EventPagination(PageNumberPagination):
    """
    Pagination class
    sets page size of json response to 100
    """
    page_size = 25


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by("-time")
