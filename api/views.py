from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import Http404

from rest_framework.generics import RetrieveAPIView
from lab_user.serializers import LabUserSerializer
from part.serializers import PartSerializer

from lab_user.models import LabUser
from part.models import Part


class CheckHashAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]  # TODO
    lookup_field = "hash_value"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entity = None
        self.is_optional = False

    def get_serializer(self, *args, **kwargs):
        if self.entity == "lab_user":
            serializer = LabUserSerializer(*args, **kwargs)
        else:
            serializer = PartSerializer(*args, **kwargs)
        return serializer

    def get_object(self):  # REFACTOR
        hash_value = self.kwargs.get("hash_value")

        entity = Part.objects.filter(hash_value=hash_value).first()
        self.entity = "part"
        if not entity:
            entity = Part.objects.filter(hash_value_optional=hash_value).first()
            self.is_optional = True
        if not entity:
            entity = LabUser.objects.filter(key_card_hash=hash_value).first()
            self.entity = "lab_user"
        if not entity:
            entity = LabUser.objects.filter(pin_code_hash=hash_value).first()
            self.entity = "lab_user"

        if entity:
            return entity
        else:
            raise Http404

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data["entity"] = self.entity
        data["is_optional"] = self.is_optional
        return Response(data)
