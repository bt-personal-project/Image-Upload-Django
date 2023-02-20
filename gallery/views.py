from django.shortcuts import render
from gallery.models import GallerySection

def gallery(request):
    gallery = GallerySection.objects.all()
    context = {
        'gallery': gallery
    }
    return render(request, 'index.html', context)
