from django.utils import timezone
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from part.models import Part
from part.serializers import PartSerializer, UpdateStatusPartSerializer, UpdateAutoPartSerializer


class PartRetrieveAPIView(RetrieveAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()
    lookup_field = "name"


class PartListAPIView(ListAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()


class UpdatePartAutoAPIView(UpdateAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]  # TODO
    permission_classes = [IsAuthenticated]
    queryset = Part.objects.all()
    serializer_class = UpdateAutoPartSerializer
    lookup_field = "name"


class UpdatePartStatusAPIView(UpdatePartAutoAPIView):
    serializer_class = UpdateStatusPartSerializer

    def perform_update(self, serializer):
        serializer.validated_data["last_time"] = timezone.now()
        serializer.save()
