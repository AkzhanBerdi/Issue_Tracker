from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DeleteView, ListView, UpdateView, DetailView
from django.views.generic.edit import FormMixin
from .models import Issue, Status, Type, Project
from .forms import IssueForm, ProjectForm
from django.views import View
from django.urls import reverse_lazy, reverse

# Create your views here.
class ProjectView(ListView):
    model = Project
    template_name = 'project_list.html'

    def get_queryset(self):
        return self.model.objects.all()

class ProjectCreateView(View):
    template_name = 'project_create.html'

    def get(self, request):
        form = ProjectForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return redirect('main')

class ProjectDetailView(FormMixin, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project_detail.html'
    fields = ['name', 'description']
    form_class = IssueForm

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['issue'] = Issue.objects.filter(project=self.object, is_closed=False)
        context['form'] = IssueForm(initial={'project': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        form.save()
        return super(ProjectDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})