from django.shortcuts import render
from productos.models import producto

# Create your views here.

def index(request):
    
    return render(request,'index.html',{'produc':producto.objects.all()})

def imformacion(request):
    return render(request,'html/empresa.html')

def detalles(request):
    return render(request, 'html/detalles.html')

def productos(request):
    return render(request,'html/productos.html',{'produc':producto.objects.all()})