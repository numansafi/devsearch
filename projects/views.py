from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    page  = 'Projects'
    context= {'page':page, 'projects':projectsList}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request,'projects/single-project.html',{'project':projectObj})
