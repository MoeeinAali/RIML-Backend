from unfold.admin import ModelAdmin
from .models import ResearchField
from django.contrib import admin
from core.admin import custom_admin_site


@admin.register(ResearchField)
class ResearchFieldAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)


custom_admin_site.register(ResearchField, ResearchFieldAdmin)
