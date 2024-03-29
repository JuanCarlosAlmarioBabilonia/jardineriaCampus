import requests
import os
from tabulate import tabulate
import modules.getGamas as gG
def getAllData():
    pet=requests.get("http://154.38.171.54:5008/productos")
    data=pet.json()
    return data
def getProductCodigo(codigo):
    pet=requests.get(f"http://154.38.171.54:5008/productos/{codigo}")
    return [pet.json()] if pet.ok else[]
# def getProductCodigo1(id):
#     pet=requests.get(f"http://154.38.171.54:5008/productos/{id}")
#     return [pet.json()] if pet.ok else[]
def getProductCodigo2(codigo):
    pet=requests.get(f"http://154.38.171.54:5008/productos/{codigo}")
    data=pet.json()
    if(len(data)==0):
        data=None
        return data
def getAllProductosOrnamentales(gama,stock):
    condiciones=[]
    for val in getAllData():
        if(val.get("gama")==gama) and (val.get("cantidadEnStock")>=stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i]={
        "Codigo del Producto":val.get("codigo_producto"),
        "Nombre":val.get("nombre"),  
        "Gama":val.get("gama"),
        "Cantidad en stock":val.get("cantidadEnStock"),  
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
            gama= gG.getAllNombre()[(int(input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))))]
            stock=int(input("Ingrese el stock del producto: "))
            print(tabulate(getAllProductosOrnamentales(gama,stock),tablefmt="grid"))
            input("Presiona cualquier tecla para continuar.....")
        elif(op==0):
            break
