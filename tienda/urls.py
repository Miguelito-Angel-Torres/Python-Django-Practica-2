#urls de la aplicacion : 

#Importacion del path
from django.urls import path
#Importacion de Vistas 
from . import views





urlpatterns = [
   
    #Apunta a la raiz
    path('',views.tienda,name="Tienda"),
   
]      



