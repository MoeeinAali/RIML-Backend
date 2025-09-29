from unfold.admin import ModelAdmin
from .models import ResearchField, JournalClub
from django.contrib import admin
from core.admin import custom_admin_site


@admin.register(ResearchField)
class ResearchFieldAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)


custom_admin_site.register(ResearchField, ResearchFieldAdmin)


@admin.register(JournalClub)
class JournalClubAdmin(ModelAdmin):
    list_display = (
        "title",
        "presenter",
        "date",
        "time",
        "attendance_type",
        "research_fields_list",
    )
    list_filter = ("attendance_type", "date",)
    search_fields = ("title", "presenter__first_name", "presenter__last_name")
    ordering = ("-date", "-time")
    autocomplete_fields = ("presenter", "research_fields")

    def research_fields_list(self, obj):
        return ", ".join(rf.name for rf in obj.research_fields.all())

    research_fields_list.short_description = "Research Fields"


custom_admin_site.register(JournalClub, JournalClubAdmin)
