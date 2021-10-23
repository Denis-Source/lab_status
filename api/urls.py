from django.urls import path
from lab_user.views import LabUserListAPIView, LabUserRetrieveAPIView, LabUserConfidentialRetrieveAPIView, UpdateStatusLabUserAPIView, LabUserListAPIViewPresent
from part.views import PartRetrieveAPIView, PartListAPIView, UpdatePartStatusAPIView, UpdatePartAutoAPIView
from message.views import MessageListAPIView, MessageCreateAPIView
from event.views import EventListAPIView, EventCreateAPIView, EventAddVideoAPIView
from api.views import CheckHashAPIView

urlpatterns = [
    path("lab-users", LabUserListAPIView.as_view(), name="lab_users"),
    path("lab-users/<str:username>", LabUserRetrieveAPIView.as_view(), name="lab_user"),
    path("lab-users-present", LabUserListAPIViewPresent.as_view(), name="lab_user_present"),
    path("lab-users/<str:username>/more", LabUserConfidentialRetrieveAPIView.as_view(), name="lab_user_confidential"),
    path("lab-users/<str:username>/status", UpdateStatusLabUserAPIView.as_view(), name="lab_user_confidential"),
    path("parts/", PartListAPIView.as_view(), name="parts"),
    path("parts/<str:name>/", PartRetrieveAPIView.as_view(), name="parts"),
    path("parts/<str:name>/status", UpdatePartStatusAPIView.as_view(), name="part_status"),
    path("parts/<str:name>/auto", UpdatePartAutoAPIView.as_view(), name="part_auto"),
    path("events/", EventListAPIView.as_view(), name="events"),
    path("events/create", EventCreateAPIView.as_view(), name="event_create"),
    path("events/<int:pk>/video", EventAddVideoAPIView.as_view(), name="event_video"),
    path("messages/", MessageListAPIView.as_view(), name="messages"),
    path("messages/create", MessageCreateAPIView.as_view(), name="create_messages"),

    path("check-hash/<str:hash_value>", CheckHashAPIView.as_view(), name="check_hash")
]
