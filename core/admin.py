from django.contrib import admin
from core.models import Project, Feature, Bug, TestCase


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    pass


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    pass


