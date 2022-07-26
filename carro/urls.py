#urls de la aplicacion : 

#Importacion del path
from django.urls import path
#Importacion de Vistas 
from . import views


#para poder usar mas solidas 
app_name="carro"


urlpatterns = [
   
    #Primer urls para agregar productos
    #Pasamos el id del producto
    path('agregar/<int:producto_id>/', views.agregar_producto,name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto,name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto,name="restar"),
    path('limpiar/', views.limpiar_carro,name="limpiar"),
   
]      



