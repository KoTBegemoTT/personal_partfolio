from django.shortcuts import render
from .models import Project

app_name = 'portfolio'


def home(request):
    projects = Project.objects.all()
    return render(request, r'portfolio\home.html', {'projects': projects})
