from rest_framework import serializers
from .models import Team, TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            'id', 'first_name', 'last_name',
            'position', 'bio', 'image', 'email', 'linkedin_url',
            'github_url', 'twitter_url', 'website_url', 'scholar_url',
        ]


class TeamSerializer(serializers.ModelSerializer):
    members = TeamMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members']
