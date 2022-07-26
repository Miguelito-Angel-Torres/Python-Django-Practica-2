from django.shortcuts import render

from blog.models import Post,Categoria



def blog(request):

    post = Post.objects.all()
    return render(request,"blog/blog.html",{"posts":post})

def categoria(request,categoria_id):
    #Listar todo los post de una categoria 

    categoria= Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias= categoria)


    return render(request,"blog/categoria.html",{'categoria':categoria,"posts":post})

