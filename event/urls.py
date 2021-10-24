from django.urls import path
from event.views import EventDetailView

urlpatterns = [
    path("<int:pk>", EventDetailView.as_view())
]
