from django.contrib import admin
from .models import Team, TeamMember


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'members_count', 'order',)
    search_fields = ('name', 'description')
    ordering = ('-order',)

    def members_count(self, obj):
        return obj.members.count()


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'position',)
    list_filter = ('team',)
    search_fields = ('first_name', 'last_name', 'email', 'position')
    ordering = ('-created_at',)
    autocomplete_fields = ('team',)
