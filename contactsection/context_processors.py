from .models import ContactSection, ContactDetails

def contact_context(request):
    cs = ContactSection.objects.all()
    cd = ContactDetails.objects.all()
    
    context = {
        'cs': cs,
        'cd': cd,
    }
    
    return (context)