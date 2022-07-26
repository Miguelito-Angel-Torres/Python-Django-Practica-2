from django.contrib import admin

from .models import Servicio

# Aqui se Registra la Aplicacion
    

#Para que aparezca el created y updated
class ServicioAdmin(admin.ModelAdmin):
    #Son solo lectura : Con la propiedad readonly_fields
    readonly_fields =('created','updated')
    #search_fields =('titulo')
    








admin.site.register(Servicio,ServicioAdmin)

