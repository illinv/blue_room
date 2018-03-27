from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from core.models import Project
from api.v1.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]