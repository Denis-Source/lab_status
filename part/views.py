from rest_framework.generics import ListAPIView

from part.models import Part
from part.serializers import PartSerializer


class PartListAPIView(ListAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()
