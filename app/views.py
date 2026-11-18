from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.filter(is_active=True).order_by('order')
    return render(request, 'index.html', {'projects': projects})


def profile(request):
    # ✅ FIX: lowercase 'profile.html' — Linux case-sensitive
    return render(request, 'profile.html')
