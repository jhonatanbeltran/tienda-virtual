from django.contrib import admin
from django.contrib.auth.models import User,Group
from productos import models


class categoriaAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
    search_fields = ['nombre']

class marcaAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','img']
    search_fields = ['nombre']

class productoAdmin(admin.ModelAdmin):
    search_fields = ['marca__nombre','categoria__nombre']
    list_display=['referencia','nombre','descripcionCorta','detalle','valor','keywords','categoria','marca']
    list_filter=['marca__nombre','categoria__nombre']
   
class empresaAdmin(admin.ModelAdmin):
    list_display=['referencia','quienesSomos','email','direccion','telefono','facebook','twitter','instagram']

admin.site.register(models.categoria,categoriaAdmin)
admin.site.register(models.marca,marcaAdmin)
admin.site.register(models.empresa)
admin.site.register(models.producto,productoAdmin)
admin.site.site_header='Administracion total de la tienda'
admin.site.unregister(User)
admin.site.unregister(Group)


# Register your models here.
