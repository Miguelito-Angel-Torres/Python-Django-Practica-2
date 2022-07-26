from django.db import models
# App para nuestro servicio
# mapeo Orm
# Esto es creacion de tablas
class Servicio(models.Model):
    #Campo que queremo que tenga nuestro pagina servicio

    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # Con el upload_to  le indica q se crea una subcarpeta llamado servicios
    imagen = models.ImageField(upload_to='servicios')
    #La fecha que se creo un servicio:
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True para que se haga automaticamente
    #la fecha que se modifico:
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        #Verificar el nombre que tendra ese servicio en la base de datos
        verbose_name ='servicio'
        verbose_name_plural = 'servicios'

    
    #Para que nos devuelva el titulo del servicio:
    def __str__(self):
        return self.titulo
    
    #Tenemos que hacer la Migracion
    #python manage.py makemigration
    #python manage.py migrate

    #Para imagenes necesitas Pillow 


