from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.
#Servicios
def servicios(request):
    #creacion de una variable
    # Esta forma todo los servicios(variables ) que hemos construidos
    servicios =Servicio.objects.all()
    # El nombre de lavariable : servicios , esta forma le digo qcarge todo los servicios
    return render(request,"servicios/servicios.html",{"servicios":servicios})
