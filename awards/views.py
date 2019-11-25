from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')


def search_project(request):
    try:
        if 'project' in request.GET and request.GET['project']:
            searched_term = (request.GET.get('project')).title()
            searched_project = Project.objects.get(project_title__icontains = searched_term.title())
            return render(request,'search.html',{'project':searched_project})
    except (ValueError,Project.DoesNotExist):
        raise Http404()

    return render(request,'search.html')