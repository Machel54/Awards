from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile,Project
from django.db.models import Max,F
from .forms import NewProjectForm,VoteForm,ProfileEditForm

# Create your views here.
def index(request):
    projects = Project.objects.all()
    best_rating = 0
    best_project = Project.objects.annotate(max=Max(F('content')+ F('design')+ F('usability'))).order_by('-max').first()
    # best_rating = (best_project.design + best_project.usability + best_project.content)/3
    for project in projects:
        average = (project.design + project.usability + project.content)/3
        best_rating = round(average,2)
    return render(request,'index.html',{'projects':projects,'best_rating':best_rating,'best_project':best_project})


def search_project(request):
    try:
        if 'project' in request.GET and request.GET['project']:
            searched_term = (request.GET.get('project')).title()
            searched_project = Project.objects.get(project_title__icontains = searched_term.title())
            return render(request,'search.html',{'project':searched_project})
    except (ValueError,Project.DoesNotExist):
        raise Http404()

    return render(request,'search.html')

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    project = Project.objects.get(id=project_id)
    rating = round(((project.design + project.usability + project.content)/3),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            project.vote_submissions += 1
            if project.design == 0:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 0:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 0:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
            return redirect(reverse('project',args=[project.id]))
    else:
        form = VoteForm()
    return render(request,'project.html',{'form':form,'project':project,'rating':rating})