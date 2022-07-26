from django.contrib import admin

#Importar de models la categoria como el post

from .models import Categoria,Post

# Register your models here.

#Panel de administracion:

class CategoriaADMIN(admin.ModelAdmin):
    readonly_fields =('created','updated')


class PostADMIN(admin.ModelAdmin):
    readonly_fields =('created','updated')


admin.site.register(Categoria,CategoriaADMIN)
admin.site.register(Post,PostADMIN)