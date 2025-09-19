from django.contrib import admin
from .models import Publisher, Publication, PublicationBadge, PublicationBadgeLink


class PublicationBadgeLinkInline(admin.TabularInline):
    model = PublicationBadgeLink
    extra = 1
    autocomplete_fields = ["badge"]


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
    inlines = [PublicationBadgeLinkInline]


@admin.register(PublicationBadge)
class PublicationBadgeAdmin(admin.ModelAdmin):
    list_display = ("name", "label", "link")
    search_fields = ("name", "label")
