from django.urls import path
from . import views

urlpatterns= [
    path('', views.herosection, name='herosection'),
]