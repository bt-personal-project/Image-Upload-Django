from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contact"),
    path('', views.contactsection, name="contactsection"),
    path('', views.contactdetails, name="contactdetails"),
]