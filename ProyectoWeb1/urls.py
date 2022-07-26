#Urls del Proyecto
from django.contrib import admin
from django.urls import path,include

#Primero Importe las Vista para hacer una prueba from ProyectoWebApp import views
# Eso sirve para enclacer diferentes aplicaciones
urlpatterns = [
    path('admin/', admin.site.urls),

    # Servicios

    path('servicios/', include('servicios.urls')),

    #Irnos a nuestra Aplicacion

    path('blog/',include('blog.urls')),

    path('contacto/',include('contacto.urls')),


    path('',include('ProyectoWebApp.urls')),

    path('tienda/',include('tienda.urls')),

    path('carro/',include('carro.urls')),
   
    

]      




#Este urls es para todas las aplicaciones que forma parte de este proyecto
#Directorio General Proyecto