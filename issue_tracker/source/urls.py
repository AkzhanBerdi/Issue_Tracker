"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tracker.issues_view import (
    IssueTemplateView, 
    IssueDetailView, 
    IssueCreateView,
    IssueEditView,
    IssueDeleteView,
)
from tracker.projects_view import (
    ProjectView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectEditView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectView.as_view(), name='main'),

    path('project_detail/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project_create', ProjectCreateView.as_view(), name='project_create'),
    path('project_delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    path('project_edit/<int:pk>', ProjectEditView.as_view(), name='project_edit'),

    path('issue_list', IssueTemplateView.as_view(), name='issue_list'),
    path('issue_detail/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('issue_create', IssueCreateView.as_view(), name='issue_create'),
    path('issue_edit/<int:pk>', IssueEditView.as_view(), name='issue_edit'),
    path('issue_delete/<int:pk>', IssueDeleteView.as_view(), name='issue_delete'),
]