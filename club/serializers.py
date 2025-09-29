from rest_framework import serializers

from core.serializers import TeamMemberSerializer
from .models import ResearchField, JournalClub


class ResearchFieldListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchField
        fields = ['name', 'image', ]


class ResearchFieldDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchField
        fields = ['name', 'image', 'markdown', ]


class JournalClubListSerializer(serializers.ModelSerializer):
    research_fields = ResearchFieldListSerializer(many=True, read_only=True)

    class Meta:
        model = JournalClub
        fields = ['title', 'date', 'time', 'attendance_type', 'research_fields', ]


class JournalClubDetailSerializer(serializers.ModelSerializer):
    research_fields = ResearchFieldListSerializer(many=True, read_only=True)
    presenter = TeamMemberSerializer(read_only=True)

    class Meta:
        model = JournalClub
        fields = ['title', 'date', 'time', 'attendance_type', 'research_fields', 'presenter', 'markdown']
