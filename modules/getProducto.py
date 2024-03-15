import requests
import os
from tabulate import tabulate
def getAllData():
    pet=requests.get("http://172.16.100.133:5503")
    data=pet.json()
    return data
def getProductCodigo(codigo):
    for val in getAllData():
        if(val.get("codigo_producto") == codigo):
            return [val]
def getAllProductosOrnamentales(gama,stock):
    condiciones=[]
    for val in getAllData():
        if(val.get("gama")==gama) and (val.get("cantidad_en_stock")>=stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i]={
        "Codigo del Producto":val.get("codigo_producto"),
        "Nombre":val.get("nombre"),  
        "Gama":val.get("gama"),  
        "Cantidad en stock":val.get("cantidad_en_stock"),  
        "Precio de venta":val.get("precio_venta"),  
        "Precio al proveedor":val.get("precio_proveedor")      
    }  
    return condiciones
def menu():
    while True:
        os.system("clear")
        print("""
REPORTES DE LOS PRODUCTOS
0. Regresar al menu principal
1. Obtener productos de una categoria ordenando su precio de venta y rectificando que su cantidad de stock sea superior
""")
        op=int(input("Seleccione una de las opciones: "))
        if (op==1):
            gama= input("Ingrese la gama: ")
            stock=int(input("Ingrese el stock del producto: "))
            print(tabulate(getAllProductosOrnamentales(gama,stock),tablefmt="grid"))
            input("Presiona cualquier tecla para continuar.....")
        elif(op==0):
            break
