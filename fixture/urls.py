from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixture, name="fixture"),
    path('', views.fixturesection, name="fixturesection"),
    path('', views.premierleaguetable, name="premierleaguetable"),
    
]