from .models import News, ImageUpload

def news_context(request):
    newscontext = News.objects.all()
    imagecontext = ImageUpload.objects.all()
    
    context = {
        'newscontext': newscontext,
        'imagecontext': imagecontext,
    }
    
    return (context)