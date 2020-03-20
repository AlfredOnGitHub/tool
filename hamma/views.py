from django.shortcuts import render 
from .forms import Registro
   
# Create your views here. 
def registrarse(request): 
    context ={} 
    context['form']= Registro() 
    return render(request, "hamma/portal.html", context) 

def index(request):
    return render(request, "hamma/index.html")