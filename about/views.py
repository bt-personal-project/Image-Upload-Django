from django.shortcuts import render
from .models import AboutSection

# Create your views here.
def aboutsection(request):
    about = AboutSection.objects.all()
    
    context = {
        'about': about,
    }
    return render(request, 'about/index.html', context)