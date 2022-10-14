from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm
# Create your views here.
#static url call response
"""projectList=[
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
]"""
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

#for creating the new project
def create_project(request):
    form=ProjectForm()

    if request.method== 'POST':
        #just printing the fields entered by the user
        #print(request.POST) 
        # add the form data into the database and after submit redirect to the project page display the project
        form=ProjectForm(request.POST,request.FILES)

        #check all the fields are entered (validated)
        if form.is_valid():
            # save the values into the db
            form.save()
            #redirect to the project page
            return redirect('projects')          
            
    context={'form':form}
    return render(request,'projects/project_form.html',context)

#for modify/update the already existing project
def update_project(request,pk):

    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)

    if request.method== 'POST':
        #just printing the fields entered by the user
        #print(request.POST) 
        # add the form data into the database and after submit redirect to the project page display the project
        form=ProjectForm(request.POST,request.FILES,instance=project)

        #check all the fields are entered (validated)
        if form.is_valid():
            # save the values into the db
            form.save()
            #redirect to the project page
            return redirect('projects')          
            
    context={'form':form}
    return render(request,'projects/project_form.html',context)

def delete_project(request,pk):
    project=Project.objects.get(id=pk)
    if request.method== 'POST':
        project.delete()
        return redirect('projects')
    
    context={'object':project}
    return render(request,'projects/delete_project.html',context)