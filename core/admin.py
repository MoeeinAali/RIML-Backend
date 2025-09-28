from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from .models import Team, TeamMember
from unfold.admin import ModelAdmin
from unfold.sites import UnfoldAdminSite
from django.contrib import admin


class CustomAdminSite(UnfoldAdminSite):
    site_title = "RIML - Admin "
    index_title = "RIML Admin Panel"


custom_admin_site = CustomAdminSite(name='custom_admin')


@admin.register(Team)
class TeamAdmin(ModelAdmin):
    list_display = ('name', 'members_count', 'order',)
    search_fields = ('name', 'description')
    ordering = ('-order',)

    def members_count(self, obj):
        return obj.members.count()


@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'position',)
    list_filter = ('team',)
    search_fields = ('first_name', 'last_name', 'email', 'position')
    ordering = ('-created_at',)
    autocomplete_fields = ('team',)


custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, GroupAdmin)
custom_admin_site.register(TeamMember, TeamMemberAdmin)
custom_admin_site.register(Team, TeamAdmin)
