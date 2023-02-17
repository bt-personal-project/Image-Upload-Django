from django.shortcuts import render
from .models import FixtureSection, PremierLeagueTable

# Create your views here.
def fixturesection(request):
    fixture = FixtureSection.objects.all()

    context = {
        'fixture': fixture,
    }

    return render(request, 'fixture/index.html', context)

def premierleaguetable(request):
    table = PremierLeagueTable.objects.all()
    
    context = {
        'table': table,
    }

    return render(request, 'fixture/index.html', context)
