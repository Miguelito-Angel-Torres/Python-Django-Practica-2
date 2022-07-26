from django.urls import path

from . import views


urlpatterns = [

    path('',views.blog,name="Blog"),
    #CREACION DE LA URLS DEL HTMOL CATEGORIAS:

    # categoria_id : Es especificacion el parametro,
    path('categoria/<int:categoria_id>/',views.categoria,name="categoria")
]


