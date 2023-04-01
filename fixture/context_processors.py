from .models import FixtureSection, PremierLeagueTable

def fixture_context(request):
    fs = FixtureSection.objects.all()
    pt = PremierLeagueTable.objects.all()
    
    context = {
        'fs': fs,
        'pt': pt
    }
    
    return(context)