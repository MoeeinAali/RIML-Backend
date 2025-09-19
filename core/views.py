from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Team
from .serializers import TeamSerializer


class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AllowAny]

