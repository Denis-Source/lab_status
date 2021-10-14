from django.urls import path
from lab_user.views import LabUserRetrieveAPIView, LabUserConfidentialRetrieveAPIView
from part.views import PartListAPIView
from message.views import MessageListAPIView, MessageCreateAPIView
from event.views import EventListAPIView

urlpatterns = [
    path("lab-users/<str:username>", LabUserRetrieveAPIView.as_view(), name="lab_user"),
    path("lab-users/<str:username>/more", LabUserConfidentialRetrieveAPIView.as_view(), name="lab_user_confidential"),
    path("parts/", PartListAPIView.as_view(), name="parts"),
    path("events/", EventListAPIView.as_view(), name="events"),
    path("messages/", MessageListAPIView.as_view(), name="messages"),
    path("messages/create", MessageCreateAPIView.as_view(), name="create_messages"),
]
