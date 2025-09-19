from rest_framework import serializers
from .models import Publication, Publisher, PublicationBadge
from core.serializers import TeamMemberSerializer


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'year', 'logo',]


class PublicationBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationBadge
        fields = ['id', 'name', 'label', 'link']


class PublicationListSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(read_only=True)
    publication_badges = PublicationBadgeSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = [
            'id', 'title', 'authors', 'publisher', 'publication_badges',
        ]


class PublicationDetailSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(read_only=True)
    publication_badges = PublicationBadgeSerializer(many=True, read_only=True)
    team_members = TeamMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = [
            'id', 'title', 'authors', 'publisher', 'publication_badges',
            'team_members'
        ]
