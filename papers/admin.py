from unfold.admin import ModelAdmin
from .models import Publisher, Publication, PublicationBadge
from core.admin import custom_admin_site
from django.contrib import admin


@admin.register(Publisher)
class PublisherAdmin(ModelAdmin):
    list_display = ("name", "year",)
    search_fields = ("name",)
    list_filter = ("year",)


@admin.register(Publication)
class PublicationAdmin(ModelAdmin):
    list_display = ("title", "authors", "publisher",)
    search_fields = ("title", "authors", "publisher__name")
    list_filter = ("publisher",)
    autocomplete_fields = ["publisher", "team_members", "publication_badges"]


@admin.register(PublicationBadge)
class PublicationBadgeAdmin(ModelAdmin):
    list_display = ("name", "label", "link")
    search_fields = ("name", "label", "link")


custom_admin_site.register(Publisher, PublisherAdmin)
custom_admin_site.register(Publication, PublicationAdmin)
custom_admin_site.register(PublicationBadge, PublicationBadgeAdmin)
