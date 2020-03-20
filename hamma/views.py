from django.shortcuts import render
from django.http import HttpResponse
from time import sleep

from .forms import Registro

def index(request):
    return render(request, 'hamma/index.html', {})

def registrarse(request):
    form = Registro()
    return render(request, 'hamma/registro.html', {})
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            Registro.save()
            return HttpResponse('Done. Wait.')
            sleep(5)
            return render(request, 'hamma/index.html')
        else:
            form = Registro()
        return HttpResponse('debuggin')


# def registrarse(request):
#     if request.method == "POST":
#         form = Registro(request.POST)
#         if form.is_valid():
#             Registro.save()
#             return HttpResponse('Done. Wait.')
#             sleep(5)
#             return render(request, 'hamma/registro.html')
#         else:
#             form = Registro()
#         return HttpResponse('debuggin')