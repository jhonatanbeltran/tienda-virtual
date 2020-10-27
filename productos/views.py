from django.conf import settings
from django.shortcuts import render
from productos.models import producto,empresa,categoria,marca
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.db.models import Q

# Create your views here.
def send_email(email,asunto):
    contex={'email':email}
    template=get_template('html/correo.html')
    content=template.render(contex)
    mail=EmailMultiAlternatives(
        'Correo de floop',
        asunto,
        settings.EMAIL_HOST_USER,
        [email],
        )

    mail.attach_alternative(content,'text/html')
    mail.send()

def contacto(request):
    if request.method=='POST':
        email=request.POST.get('email','')
        asunto=request.POST.get('asunto','')
        print(email,asunto)
        send_email(email,asunto)
    return render(request,'index.html')


def index(request):
    empre=empresa.objects.all()[0]
    empre.quienesSomos=strip_tags(empre.quienesSomos)
    productos=producto.objects.all()
    productos=list(productos)
    if productos.__len__()>=8:
        productos=productos.__reversed__()
        x=list(productos)[0:8]
    else:
        productos=productos.__reversed__()
    return render(request,'index.html',{'produc':x,'empresa':empre})

def filtroCategoria(request,idCategoria):
    cate=categoria.objects.all()
    mar=marca.objects.all()
    empre=empresa.objects.all()[0]
    prod=producto.objects.filter(categoria=idCategoria)
    x=categoria.objects.get(id=idCategoria).nombre
    return render(request,'html/productos.html',{'produc':prod,'empresa':empre,'marca':mar,'categoria':cate,'filtro':x})

def imformacion(request):
    empre=empresa.objects.all()[0]
    return render(request,'html/empresa.html')

def detalles(request,idProducto):
    isd=idProducto
    empre=empresa.objects.all()[0]
    pro=producto.objects.filter(id=isd)[0]
    
    return render(request, 'html/detalles.html',{'pro':pro,'empresa':empre})

def productos(request):
    empre=empresa.objects.all()[0]
    cate=categoria.objects.all()
    mar=marca.objects.all()
    return render(request,'html/productos.html',{'produc':producto.objects.all(),'empresa':empre,'marca':mar,'categoria':cate})

def filtroMarca(request,idMarca):
    cate=categoria.objects.all()
    mar=marca.objects.all()
    empre=empresa.objects.all()[0]
    prod=producto.objects.filter(marca=idMarca)
    x=marca.objects.get(id=idMarca).nombre
    return render(request,'html/productos.html',{'produc':prod,'empresa':empre,'marca':mar,'categoria':cate,"filtro":x})
