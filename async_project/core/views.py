# async_project/views.py
import asyncio
from django.http import JsonResponse

async def timer_view(request):
    # contador simples de 5 segundos
    result = []
    for i in range(1, 6):
        await asyncio.sleep(1)  # espera 1 segundo sem travar o servidor
        result.append(f"{i} segundo(s) passaram")

    return JsonResponse({"contador": result})
