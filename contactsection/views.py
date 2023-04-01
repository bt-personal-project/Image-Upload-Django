from django.shortcuts import render
from .models import ContactSection, ContactDetails

def contact(request):
    return render(request, 'contact.html')

def contactsection(request):
    contact = ContactSection.objects.all()
    context = {
        'contact': contact
    }
    return render(request, 'contactsection/index.html', context)

def contactdetails(request):
    contactdetails = ContactDetails.objects.all()
    context = {
        'contactd': contactdetails
    }
    return render(request, 'contactsection/index.html', context)
