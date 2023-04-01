from django.shortcuts import render
from .models import AboutSection

def about(request):
    return render(request, 'about.html')

def aboutsection(request):
    about = AboutSection.objects.all()
    
    context = {
        'about': about,
    }
    return render(request, 'about/index.html', context)