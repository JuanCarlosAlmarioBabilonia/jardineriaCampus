import storage.producto as pr
from tabulate import tabulate
def getAllProductosOrnamentales(gama, stock):
    condiciones=[]
    for val in pr.producto:
        if(val.get("gama")==gama) and (val.get("precio_venta")>=stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i]={
        "Codigo del Producto":val.get("codigo_producto"),
        "Nombre":val.get("nombre"),  
        "Gama":val.get("gama"),  
        "Dimensiones":val.get("dimensiones"),  
        "Proveedor":val.get("proveedor"), 
        "Descripcion":f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
        "Cantidad en stock":val.get("cantidad_en_stock"),  
        "Precio de venta":val.get("precio_venta"),  
        "Precio al proveedor":val.get("precio_proveedor")      
    }  
    return condiciones
def menu():
    while True:
        print("""
REPORTES DE LOS PRODUCTOS
0. Regresar al menu principal
1. Obtener productos de una categoria ordenando su precio de venta y rectificando que su cantidad de stock sea superior
""")
        op=int(input("Seleccione una de las opciones: "))
        if (op==1):
            gama=input("Ingrese la gama del producto: ")
            stock=int(input("Ingrese el stock del producto: "))
            print(tabulate(getAllProductosOrnamentales(gama,stock),headers="keys",tablefmt="grid"))
        elif(op==0):
            break
