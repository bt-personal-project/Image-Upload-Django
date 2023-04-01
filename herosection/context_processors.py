from .models import HeroSection

def hero_context(request):
    hc = HeroSection.objects.latest('id')
    return{'hc':hc}