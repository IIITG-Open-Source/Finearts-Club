from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-id')[:6]
    coordinators = Coordinator.objects.all().order_by('-id')[:6]
    return render(request, 'index.html', {'posts': posts, 'coordinators': coordinators})
