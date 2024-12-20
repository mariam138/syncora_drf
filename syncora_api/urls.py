"""
URL configuration for syncora_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from syncora_api.serializers import CustomRegisterView
from .views import home_route

urlpatterns = [
    path("", home_route),
    path("", include("profiles.urls")),
    path("", include("tasks.urls")),
    path("", include("events.urls")),
    path("", include("notes.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "dj-rest-auth/registration/",
        CustomRegisterView.as_view(),
        name="rest_registration",
    ),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    # Added for the email view from all auth as dj-rest-auth
    # relies on allauth
    # prevents 500 error when user signs up with an e-mail
    # Solution from:
    # https://github.com/Tivix/django-rest-auth/issues/534#issuecomment-491849803
    path("accounts/", include("allauth.urls")),
]
