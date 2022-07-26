#urls de la aplicacion : 

#Importacion del path
from django.urls import path
#Importacion de Vistas 
from . import views

#Para sus las dos variables de media
from django.conf  import settings
from django.conf.urls.static import static



urlpatterns = [
   
    path('',views.servicios,name="Servicios"),
  

]      

#Agregacion:

