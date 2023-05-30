from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DeleteView, ListView, UpdateView
from .models import Issue, Status, Type
from .forms import IssueForm
from django.views import View
from django.urls import reverse_lazy

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

class CustomTemplateView(ListView):
    # issue = Issue.objects.all()
    
    # def get(self, request, *args, **kwargs):
    #     return render(request, 'index.html', context={'issue': self.issue})
    model = Issue
    template_name = 'list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_closed=False)


class CustomDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        # status = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(
                        request, 
                        'detail.html', 
                        context={
                                'issue': issue
                                 #'status': status
                                }
                    )

class CustomCreateView(View):
    template_name = 'create.html'

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


class CustomEditView(UpdateView):
    template_name = 'edit.html'

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

class CustomDeleteView(DeleteView):
    model = Issue
    template_name = 'delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('issue_list')

# class CustomListView(ListView):
#     model = Issue
#     template_name = 'list.html'

#     def get_queryset(self):
#         return self.model.objects.filter(is_deleted=False)