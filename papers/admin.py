from django.contrib import admin
from .models import Publisher, Publication


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "year")
    search_fields = ("name",)
    list_filter = ("year",)
    ordering = ('-created_at',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher",)
    search_fields = ("title", "authors", "publisher__name", "publisher__year")
    list_filter = ("publisher", "publisher__year")
    ordering = ('-created_at',)
    autocomplete_fields = ["publisher"]
