import json
import requests
from tabulate import tabulate
import modules.getGamas as gG
import os
def postProducto():
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre":input("Ingrese el nombre del producto: "),
        "gama":gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones":input("Ingrese la dimensiones del producto: "),
        "proveedor":input("Ingrese el proveedor del producto: "),
        "descripcion":input("Ingrese la descripcion del producto: "),
        "cantidad_en_stock":int(input("Ingrese la cantidad en stock: ")), 
        "precio_venta":int(input("Ingrese el precio de venta: ")), 
        "precio_proveedor":int(input("Ingrese el precio al proveedor: "))
        }
    pet=requests.post("http://192.168.20.37:5503", data=json.dumps(producto))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE PRODUCTOS
1.Guardar un producto
0.Atras
              """)
        op = int(input("Selecione una de las opciones: "))
        if(op== 1):
            print(tabulate(postProducto(),tablefmt="grid"))
            input("Precione una tecla para continuar.....")
        elif(op== 0):
            break