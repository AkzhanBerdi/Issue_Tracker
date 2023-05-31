from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DeleteView, ListView, UpdateView, DetailView
from .models import Issue, Status, Type, Project
from .forms import IssueForm
from django.views import View
from django.urls import reverse_lazy

# Create your views here.

class IssueTemplateView(ListView):
    model = Issue
    template_name = 'issue_list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_closed=False)


class IssueDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        return render(request, 'issues_detail.html', context={'issue': issue})

class IssueCreateView(View):
    template_name = 'issue_create.html'

    def get(self, request):
        form = IssueForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
        else:
            return redirect('main')


class IssueEditView(UpdateView):
    template_name = 'issue_edit.html'

    def get(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        form = IssueForm(instance=issue)
        return render(request, self.template_name, {'form': form, 'issue': issue})

    def post(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
        print(form.errors)
        return redirect('main')

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('issue_list')
