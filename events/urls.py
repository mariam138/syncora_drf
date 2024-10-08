from django.urls import path
from .views import EventList, CreateEvent

urlpatterns = [
    path("events/", EventList.as_view(), name="event_list"),
    path("events/new/", CreateEvent.as_view(), name="create_event"),
]