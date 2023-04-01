from .models import AboutSection

def about_context(request):
    aboutcontext  = AboutSection.objects.all()
    context = {
        'aboutcontext': aboutcontext
    }
    return (context)