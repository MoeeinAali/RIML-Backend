from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import GalleryImage
from papers.views import CustomPagination
# Create your views here.
class GalleryImageListView(generics.ListAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageListSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination