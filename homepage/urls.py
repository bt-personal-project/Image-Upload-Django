from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.homepage, name="homepage"),
    path('news', views.news, name="news"),
    path('news/<slug>', views.show_post, name='show_post'),
]