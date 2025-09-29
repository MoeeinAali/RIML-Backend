from rest_framework import serializers
from .models import GalleryImage


class GalleryImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'image',]
