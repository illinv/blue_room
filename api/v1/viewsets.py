from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Project, Feature, Bug, TestCase
from api.v1.serializers import ProjectSerializer, FeatureSerializer, BugSerializer, TestCaseSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)

    @detail_route(methods=['get'])
    def features(self, request, pk=None):
        queryset = Project.objects.get_features_by_project_id(pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def bugs(self, request, pk=None):
        queryset = Project.objects.get_bugs_by_project_id(pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FeatureViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('project', )


class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('feature', )


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('feature', )
