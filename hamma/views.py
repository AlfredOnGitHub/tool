from django.shortcuts import render

def nuevo_usuario(request):
    return render(request, 'hamma/nuevo_usuario.html', {})