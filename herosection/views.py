from django.shortcuts import render
from .models import HeroSection

def herosection(request):
    hero = HeroSection.objects.all()

    context = {
        'hero': hero,
    }
    return render(request, 'herosection/index.html', context)
