from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from core.models import Project, Feature, Bug, TestCase


class ProjectListView(ListView):
    model = Project
    template_name = 'project-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        project = context['object']
        context['in_work'] = Project.objects.get_in_work_features_and_bugs(project.pk)
        return context


class FeatureDetail(DetailView):
    model = Feature
    template_name = 'feature-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feature = context['object']
        bugs = Bug.objects.filter(feature=feature)
        test_cases = TestCase.objects.filter(feature=feature)
        context['bugs'] = bugs
        context['test_cases'] = test_cases
        return context
