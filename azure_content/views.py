from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm  # We'll create this form instead of using fields manually

def home_view(request):
    projects = Project.objects.all()
    return render(request, "azure_content/home.html", {'project_list': projects})

def about_view(request):
    return render(request, "azure_content/about.html")

def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, "azure_content/create.html", {'form': form})

def project_edit_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    return render(request, "azure_content/create.html", {'form': form})

def project_delete_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    return render(request, "azure_content/delete.html", {'project': project})
