class Carro:
    #La peticion request para hacer al carro
    def __init__(self,request):
        #Almacenar la peticion actual
        self.request = request
        self.session=request.session
         #Construir una carro de compra
        carro = self.session.get("carro")
        if not carro:
            #El carro es un diccionario:
            carro=self.session["carro"]={}
        
        self.carro=carro

        
    def agregar(self,producto):
        if(str(producto.id)not in self.carro.keys()):

            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url

            }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    #el precio
                    value["precio"] =float( value["precio"])+producto.precio
                    break
         #LLAMAR FUNCION
        self.guardar_carro()

    def guardar_carro(self):
        #Actualizar carro
        #elemento "carro"
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)

        if producto.id in self.carro:
            #Quitar producto: Aca le estoy diciento
            #que quite el producto del carro con la identificacion id
            del self.carro[producto.id]
            self.guardar_carro()

    
    def restar_productos(self,producto):
        for key,value in  self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                # restar articulos
                value["precio"] =float( value["precio"])-producto.precio
                if value["cantidad"] <1:
                    self.eliminar(producto)

                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True



