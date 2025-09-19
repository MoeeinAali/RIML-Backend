from django.urls import path
from .views import (
    TeamListAPIView,
)

urlpatterns = [
    # Teams with members
    path('teams/', TeamListAPIView.as_view(), name='team-list'),
]
