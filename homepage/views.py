from django.shortcuts import render
from django.http import Http404, HttpResponse
from homepage.models import ImageUpload
# from .models import POST

def homepage(request):
    # image = ImageUpload.objects.get(pk=image_id)
    # if image is not None:
    #     return render(request, 'homepage/index.html', {'image': image} )
    # else:
    #     raise Http404("Image doesn't exist")

    image = ImageUpload.objects.all()
    context = {'image': image}

    return render(request, 'homepage/index.html', context )

def news(request):
    image = ImageUpload.objects.all()
    context = {'image': image}
    return render(request, 'homepage/news.html', context)


def show_post(request, slug):
    post = ImageUpload.objects.get(slug=slug)
    return render(request, 'homepage/inside.html', {'post': post})