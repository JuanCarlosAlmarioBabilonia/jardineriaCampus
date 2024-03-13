import requests
import json
from tabulate import tabulate
import modules.postProducto as psp
def getAllData():
    pet=requests.get("http://172.16.100.133:5503")
    data=pet.json()
    return data
def getAllProductosOrnamentales(gama, stock):
    condiciones=[]
    for val in getAllData:
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
2. Guardar datos
""")
        op=int(input("Seleccione una de las opciones: "))
        if (op==1):
            gama=input("Ingrese la gama del producto: ")
            stock=int(input("Ingrese el stock del producto: "))
            print(tabulate(getAllProductosOrnamentales(gama,stock),headers="keys",tablefmt="grid"))
        elif(op==2):
            producto = {
            "Codigo del Producto": input("Ingrese el codigo del producto: "),
            "Nombre":input("Ingrese el nombre del producto: "),
            "Gama":input("Ingrese la gama del producto: "),
            "Dimensiones":input("Ingrese la dimensiones del producto: "),
            "Proveedor":input("Ingrese el proveedor del producto: "),
            "Descripcion":input("Ingrese la descripcion del producto: "),
            "Cantidad Stock":int(input("Ingrese la cantidad en stock: ")), 
            "Precio de venta":int(input("Ingrese el precio de venta: ")), 
            "Precio al proveedor":int(input("Ingrese el precio al proveedor: "))
        }
            psp.postProducto(producto)
            print("Producto Guardado")
        elif(op==0):
            break
