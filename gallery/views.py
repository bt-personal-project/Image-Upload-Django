from django.shortcuts import render
from gallery.models import GallerySection

def gallery(request):
    # gallery = GallerySection.objects.all()
    # context1 = {
    #     'gallery': gallery
    # }
    # return render(request, 'gallery.html', context1) 
    return render(request, 'gallery.html')
