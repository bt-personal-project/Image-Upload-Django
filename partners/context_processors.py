from .views import Partners

def partner_context(request):
    pc = Partners.objects.all()
    return {'pc': pc}