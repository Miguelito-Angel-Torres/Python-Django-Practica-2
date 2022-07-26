from django.db import models

#Para relacionar cada post por cada usuario
from django.contrib.auth.models import User

#Creacion de Clase:

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='categoria'
        verbose_name_plural ='categorias'
    
    def __str__(self):
        return self.nombre

    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
    #Asi le digo q sea opciono la imagen:
    imagen = models.ImageField(upload_to="blog",null= True, blank=True)
    
    # Es decir Cuando Elimina  un actor que se pueda eliminar todo lo que ha creado
    # ForeignKey llave forania para realizar la relacion entre el usuario y el post
    autor = models.ForeignKey(User,on_delete=models.CASCADE)

    # Relacion entre Post y Categorias
    categorias = models.ManyToManyField(Categoria)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='post'
        verbose_name_plural ='post'
    
    def __str__(self):
        return self.titulo


 
 

