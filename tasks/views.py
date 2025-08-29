from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 Página inicial funcionando a partir do app tasks!")
