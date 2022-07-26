#importar el Objeto HttpResponse

from django.shortcuts import render


def home(request):
    return render(request,"ProyectoWebApp/home.html")


#Aca ponias todo cuando vas a comenzar
#Ejemplo : la tienda



#def home(request):
    #return render(request,"tienda/tienda.html")

