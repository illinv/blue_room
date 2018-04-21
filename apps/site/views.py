from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from core.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-detail.html'

