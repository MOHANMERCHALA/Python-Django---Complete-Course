from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Tag
# Create your views here.
#static url call response
projectList=[
    {
        'id':'1',
        'title':"Ecommerce Website",
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This was a project where I built out my portfolio'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Awesome open source project I am still working on'
    }
]
def projects(request):
    #return HttpResponse('Here are the projects!')
    """page='projects'
    number=10"""
    #context={'page':page,'number':number,'projects':projectList}
    projects=Project.objects.all()
    context={'projects':projects}
    #return render(request,'projects/projects.html',context)
    return render(request,'projects/projects.html',context)
#dynamic url call response
def project(request,pk):
    #return HttpResponse('Single project URL'+' '+str(pk))
    """for single_project in projectList:
        if single_project['id']==pk:
            project_obj=single_project"""
    project_obj=Project.objects.get(id=pk)
    tags=project_obj.tags.all()
    return render(request,'projects/single-project.html',{'project_obj':project_obj,'tags':tags})