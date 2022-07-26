#urls de la aplicacion : 

#Importacion del path
from django.urls import path
#Importacion de Vistas 
from ProyectoWebApp import views

#Para sus las dos variables de media
from django.conf  import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name="Home"),
    #No se necesita esa urls Primero que desaparece
    #path('servicios',views.servicios,name="Servicios"),
    #path('tienda',views.tienda,name="Tienda"),
    #path('blog',views.blog,name="Blog"),
    #path('contacto',views.contacto,name="Contacto")

]      

#Agregacion:

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)