from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Publication
from .serializers import PublicationListSerializer, PublicationDetailSerializer


class CustomPagination(PageNumberPagination):
    page_size = 6
    
    def get_paginated_response(self, data):
        next_page = None
        if self.page.has_next():
            next_page = self.page.next_page_number()
        
        return Response({
            'data': data,
            'nextPage': next_page
        })


class PublicationListView(generics.ListAPIView):
    queryset = Publication.objects.select_related('publisher').prefetch_related('publication_badges')
    serializer_class = PublicationListSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class PublicationDetailView(generics.RetrieveAPIView):
    queryset = Publication.objects.select_related('publisher').prefetch_related(
        'publication_badges', 'team_members'
    )
    serializer_class = PublicationDetailSerializer
    permission_classes = [AllowAny]
