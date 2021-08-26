from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'portfolio/blog.html', context)

# Create your views here.
