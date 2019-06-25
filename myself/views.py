from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request):
  projects = Project.objects.all()
  return render (request, 'index.html',{"projects":projects})

def about(request):
  return HttpResponse(request, 'about.html')

def skills(request):
  return HttpResponse(request, 'skills.html')

def projects(request):
  return HttpResponse(request, 'projects.html')

