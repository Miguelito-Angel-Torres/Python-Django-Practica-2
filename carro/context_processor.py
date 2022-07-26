#VARIABLE GLOBAL
# Es donde tu quieras poner util
def importe_total_carro(request):
    total=0
        #USUARIO ESTA AUTENTICADO SI ES TRUE (Ahorita no esta autenticado)
    #if request.user.is_authenticated:
        #Debes recorrer todo el carro ,loe elementos q hay en el carro 
        #si suamndo los importes
    #for key,value in request.session["carro"].items():
       #total=total+float(value["precio"])

    return {"importe_total_carro":total}
    
