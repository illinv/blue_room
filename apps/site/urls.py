from django.urls import path
from .views import ProjectListView, ProjectDetailView, FeatureDetail

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('feature/<int:pk>/', FeatureDetail.as_view(), name='feature-detail'),
]
