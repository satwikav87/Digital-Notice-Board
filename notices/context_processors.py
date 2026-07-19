from .models import Institution
def branding(request):
 obj,_=Institution.objects.get_or_create(pk=1)
 return {"institution":obj}
