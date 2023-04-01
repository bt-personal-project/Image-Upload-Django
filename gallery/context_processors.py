from .views import GallerySection

def GalleryContext(request):
    gc = GallerySection.objects.all()
    return {'gc': gc}