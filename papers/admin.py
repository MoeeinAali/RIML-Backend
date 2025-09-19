from django.contrib import admin
from .models import Publisher, Publication


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "year",)
    search_fields = ("name",)
    list_filter = ("year",)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "authors", "publisher",)
    search_fields = ("title", "authors", "publisher__name")
    list_filter = ("publisher",)
    autocomplete_fields = ["publisher", "team_members"]
