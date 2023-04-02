from .models import News, ImageUpload
from django.core.paginator import Paginator

def news_context(request):
    newscontext = News.objects.all()
    # imagecontext = ImageUpload.objects.all()
    imagecontext = ImageUpload.objects.all().order_by('-date')
    
    # post = ImageUpload.objects.get(slug=slug).order_by('-date')
    
    # PAGINATOR
    news_pagination = ImageUpload.objects.all().order_by('-date')
    paginator = Paginator(news_pagination, 8)
    page_num = request.GET.get('page')
    # news_pag_num = paginator.get_page(page_num)
    imagecontext = paginator.get_page(page_num)
    
    
    context = {
        'newscontext': newscontext,
        'imagecontext': imagecontext,
        # 'news_pag_num': news_pag_num,
    }
    
    return (context)