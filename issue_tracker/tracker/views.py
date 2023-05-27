from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Issue, Status
from .forms import IssueForm

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

class CustomTemplateView(TemplateView):
    issue = Issue.objects.all()
    
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={'issue': self.issue})


class CustomDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        # status = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(
                        request, 
                        'detail.html', 
                        context={
                                'issue': issue
                                # 'status': status
                                }
                    )

class CustomCreateView(TemplateView):
    template_name = 'create.html'

    def get_name(request):
        if request.method == 'POST':
            if form.is_valid():
                issue = Issue.objects.all()
                title = request.POST.get('title')
                description = request.POST.get('description')
                _type = request.POST.get('_type')
                status = request.POST.get('status')
                Issue.objects.create(title=title, description=description, _type=_type, status=status)
                return redirect("main")

        else:
            form = IssueForm()

            return render(request, 'create.html', {'form':form})


    # type_choices = [
    #     'Task',
    #     'Bug',
    #     'Enhancement',
    # ]

    # status_choices = [
    #     'New',
    #     'In Progress',
    #     'Done',
    # ]

