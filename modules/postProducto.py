import json
import requests
from tabulate import tabulate
import modules.getGamas as gG
def postProducto():
    producto = {
        "Codigo del Producto": input("Ingrese el codigo del producto: "),
        "Nombre":input("Ingrese el nombre del producto: "),
        "Gama":gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "Dimensiones":input("Ingrese la dimensiones del producto: "),
        "Proveedor":input("Ingrese el proveedor del producto: "),
        "Descripcion":input("Ingrese la descripcion del producto: "),
        "Cantidad Stock":int(input("Ingrese la cantidad en stock: ")), 
        "Precio de venta":int(input("Ingrese el precio de venta: ")), 
        "Precio al proveedor":int(input("Ingrese el precio al proveedor: "))
        }
    pet=requests.get("http://172.16.100.133:5503", data=json.dumps(producto))
    res=pet.json()
    print("Producto guardado")
    return res
def menu():
    while True:
        print("""
ADMINISTRACION DE PRODUCTOS
1.Guardar un producto
0.Atras
              """)
        op = int(input("Selecione una de las opciones: "))
        if(op== 1):
            print(tabulate(postProducto(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(op== 0):
            break