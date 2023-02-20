from django.shortcuts import render
from .models import Partners

def partners(request):
    partners = Partners.objects.all()
    context = {
        'partners' : Partners 
    }
    return render(request, 'partners/index.html', context)
