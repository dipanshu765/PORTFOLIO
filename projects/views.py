from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Project

def index(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 4)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)

    context = {
        'projects': paged_projects
    }
    return render(request, 'projects/projects.html', context)
