from generators.generadorProducto import generadorDatosProductos
import pandas as pd

def analizarDatos():
    datos=generadorDatosProductos()
    tabla=pd.DataFrame(datos,columns=["categoria","productos"])
    tabla.to_csv("./data/productostienda.csv",index=False)
analizarDatos()