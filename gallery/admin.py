from unfold.admin import ModelAdmin
from .models import GalleryImage
from django.contrib import admin
from core.admin import custom_admin_site


@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ("id", "title", 'date',)
    search_fields = ("id", 'title',)


custom_admin_site.register(GalleryImage, GalleryImageAdmin)
