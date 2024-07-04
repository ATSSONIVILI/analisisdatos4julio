import random
def generadorDatosProductos():
    productos=["musica","tv","app","pc","cel","tablets","acceso"]
    datos = []
    for producto in productos:
        tipoProducto={}     
        categoria=random.choice(["mega","plus","basico"])
        
        tipoProducto=[producto,categoria]
        
       
               
        
        
        datos.append(tipoProducto)
    return datos

print(generadorDatosProductos())