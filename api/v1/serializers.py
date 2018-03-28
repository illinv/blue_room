from rest_framework import serializers
from core.models import Project, Feature, Bug


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        field = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ("id", "title", "description", "is_release", "project", "bugs")

