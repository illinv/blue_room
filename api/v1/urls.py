from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.v1 import viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'project', viewsets.ProjectViewSet)
router.register(r'feature', viewsets.FeatureViewSet)
router.register(r'bug', viewsets.BugViewSet)
router.register(r'test_case', viewsets.TestCaseViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]