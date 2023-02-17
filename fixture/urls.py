from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixturesection, name="fixturesection"),
    path('', views.premierleaguetable, name="premierleaguetable"),
]