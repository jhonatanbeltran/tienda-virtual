from django.db import models
from ckeditor.fields import RichTextField
class marca(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(max_length=500)
    img=models.ImageField()

    def __str__(self):
        return self.nombre
     
class categoria(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(max_length=500)
    estado=models.CharField(max_length=1)

    def __str__(self):
        return self.nombre
class empresa(models.Model):
    referencia=models.CharField(max_length=20)
    quienesSomos=RichTextField(verbose_name='quienesSomos')
    email=models.EmailField()
    direccion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=20)
    facebook=models.URLField()
    twitter=models.URLField()
    instagram=models.URLField()

class producto(models.Model):
    referencia=models.CharField(max_length=20)
    nombre=models.CharField(max_length=100)
    descripcionCorta=models.CharField(max_length=250)
    detalle=models.TextField()
    img=models.ImageField(upload_to="images")
    valor=models.DecimalField(decimal_places=1,max_digits=3)
    keywords=models.CharField(max_length=100)
    estado=models.CharField(max_length=1)
    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)
    marca=models.ForeignKey(marca,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre