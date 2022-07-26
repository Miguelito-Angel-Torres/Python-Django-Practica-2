from django.db import models
from django.db.models.deletion import CASCADE
#Pillow
# Create your models here.

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=100)
    # auto_now_add : para que se inserte en forma automatica
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CategoriaProd"
        verbose_name_plural = "CategoriasProd"
    
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaProd,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda",null=True,blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)

    #agregar 
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural="Productos"

    def  __str__(self):
        return self.nombre
        

#Migraciones:
# python manage.py  makemigrations
# python manage.py migrate