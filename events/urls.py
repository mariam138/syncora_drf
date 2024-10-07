from django.urls import path
from .views import EventList

urlpatterns = [
    path("events/", EventList.as_view(), name="event_list"),
]