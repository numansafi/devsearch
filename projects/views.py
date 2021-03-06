from typing import ContextManager
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context= {'projects':projects}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{'project':projectObj})

def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)

def updateProject(request,pk):
    # Get the project id for each project
    project = Project.objects.get(id=pk)
    # Pre-fill the form with the project data i.e title
    form = ProjectForm(instance=project)

    if request.method == "POST":
        # Have the project data within the fields of the form to update
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method =="POST":
        # Delete project from database
        project.delete()
        # redirect to 'projects' page
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete_template.html',context)
