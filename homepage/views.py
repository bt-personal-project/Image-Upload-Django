from django.shortcuts import render
from django.http import Http404, HttpResponse
from homepage.models import ImageUpload
# from .models import POST
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def homepage(request):
    # image = ImageUpload.objects.get(pk=image_id)
    # if image is not None:
    #     return render(request, 'homepage/index.html', {'image': image} )
    # else:
    #     raise Http404("Image doesn't exist")

    image = ImageUpload.objects.all()
    context = {'image': image}

    # return render(request, 'homepage/index.html', context )
    return render(request, 'index.html', context)

def news(request):
    # image = ImageUpload.objects.all()
    # context = {'image': image}
    # PAGINATOR
    news_pagination = ImageUpload.objects.all()
    paginator = Paginator(news_pagination, 8)
    page_num = request.GET.get('page')
    # news_pag_num = paginator.get_page(page_num)
    image = paginator.get_page(page_num)
    data = {
        'image': image,
        # 'news_pag_num': news_pag_num,
    }

    return render(request, 'news.html', data)
    # return render(request, 'news.html', context)


def show_post(request, slug):
    post = ImageUpload.objects.get(slug=slug)
    # PAGINATOR
    news_pagination = ImageUpload.objects.all()
    paginator = Paginator(news_pagination, 8)
    page_num = request.GET.get('page')
    news_pag_num = paginator.get_page(page_num)
    data = {
        'post': post,
        'news_pag_num': news_pag_num,
    }
    # return render(request, 'newsinner.html', {'post': post})
    return render(request, 'newsinner.html', data)
