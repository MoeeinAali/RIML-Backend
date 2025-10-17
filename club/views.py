from rest_framework import generics
from rest_framework.permissions import AllowAny
from papers.views import CustomPagination
from .models import ResearchField, JournalClub
from .serializers import (
    ResearchFieldListSerializer,
    ResearchFieldDetailSerializer,
    JournalClubListSerializer,
    JournalClubDetailSerializer
)


class ResearchFieldListView(generics.ListAPIView):
    queryset = ResearchField.objects.all()
    serializer_class = ResearchFieldListSerializer
    permission_classes = [AllowAny]


class ResearchFieldDetailView(generics.RetrieveAPIView):
    queryset = ResearchField.objects.all()
    serializer_class = ResearchFieldDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "name"
    lookup_url_kwarg = "name"


class JournalClubListView(generics.ListAPIView):
    queryset = JournalClub.objects.select_related('presenter').prefetch_related('research_fields')
    serializer_class = JournalClubListSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class JournalClubDetailView(generics.RetrieveAPIView):
    queryset = JournalClub.objects.select_related('presenter').prefetch_related('research_fields')
    serializer_class = JournalClubDetailSerializer
    permission_classes = [AllowAny]
