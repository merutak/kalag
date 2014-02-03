from django.http import HttpResponse
from tlunot.models import Tluna

def by_user(request):
    user_name = request.GET['name']
    tluna = Tluna.objects.get(user__username__icontains=user_name)
    return HttpResponse('User %s: %s'%(user_name, tluna, ))