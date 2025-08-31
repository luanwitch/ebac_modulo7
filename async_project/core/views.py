from django.http import HttpResponse
import asyncio
import datetime

async def home(request):
   
    print(f"A view 'home' foi acessada em: {datetime.datetime.now()}")

    await asyncio.sleep(5)

    return HttpResponse("Olá! Esta é uma resposta assíncrona que demorou 5 segundos para carregar.")