from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path("profiles/", ProfileList.as_view(), name="profiles_list"),
    path("profiles/<int:pk>", ProfileDetail.as_view(), name='profile_detail'),
]
