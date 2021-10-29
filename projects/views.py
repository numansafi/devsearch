from typing import ContextManager
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

def projects(request):
    projects = Project.objects.all()
    context= {'projects':projects}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{'project':projectObj})

def createProject(request):
    context = {}
    return render(request, "projects/project_form.html", context)
