from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Publication
from .serializers import PublicationListSerializer, PublicationDetailSerializer


class PublicationListView(generics.ListAPIView):
    queryset = Publication.objects.select_related('publisher').prefetch_related('publication_badges')
    serializer_class = PublicationListSerializer
    permission_classes = [AllowAny]


class PublicationDetailView(generics.RetrieveAPIView):
    queryset = Publication.objects.select_related('publisher').prefetch_related(
        'publication_badges', 'team_members'
    )
    serializer_class = PublicationDetailSerializer
    permission_classes = [AllowAny]
