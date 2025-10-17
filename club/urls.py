from django.urls import path
from .views import (
    ResearchFieldListView,
    ResearchFieldDetailView,
    JournalClubListView,
    JournalClubDetailView
)

urlpatterns = [
    # Research Field URLs
    path('research-fields/', ResearchFieldListView.as_view(), name='research-field-list'),
    path('research-fields/<str:name>/', ResearchFieldDetailView.as_view(), name='research-field-detail'),
    
    # Journal Club URLs
    path('journal-clubs/', JournalClubListView.as_view(), name='journal-club-list'),
    path('journal-clubs/<int:pk>/', JournalClubDetailView.as_view(), name='journal-club-detail'),
]
