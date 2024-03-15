import json
import requests
from tabulate import tabulate
import modules.getGamas as gG
import os
import re
import modules.getProducto as gP
def postProducto():
    producto=dict()
    while True:
        try:
            if(not producto.get("codigo_producto")):
                codigo=input("Ingrese el codigo del producto:")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$',codigo)is not None):
                    data=gP.getgetProductCodigo(codigo)
                    if(data):
                        print(tabulate(data,headers="keys", tablefmt="grid"))
                        raise Exception("El codigo producto no cumple con el estandar establecido")
                    else:
                        producto["codigo_producto"]=codigo
                else:
                    raise Exception("El codigo producto no cumple con el estandar establecido")
            if(not producto.get("nombre")):
                nombre=input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$',nombre)is not None):
                    producto["nombre"]=nombre
                    break
                else:
                    raise Exception("El codigo producto no cumple con el estandar establecido")
        except Exception as error:
            print(error)
    print(producto)
#     producto = {
#         "codigo_producto": input("Ingrese el codigo del producto: "),
#         "nombre":input("Ingrese el nombre del producto: "),
#         "gama":gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
#         "dimensiones":input("Ingrese la dimensiones del producto: "),
#         "proveedor":input("Ingrese el proveedor del producto: "),
#         "descripcion":input("Ingrese la descripcion del producto: "),
#         "cantidad_en_stock":int(input("Ingrese la cantidad en stock: ")), 
#         "precio_venta":int(input("Ingrese el precio de venta: ")), 
#         "precio_proveedor":int(input("Ingrese el precio al proveedor: "))
#         }
#     pet=requests.post("http://172.16.100.133:5503", data=json.dumps(producto))
#     res=pet.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]
# def menu():
#     while True:
#         os.system("clear")
#         print("""
# ADMINISTRACION DE PRODUCTOS
# 1.Guardar un producto
# 0.Atras
#               """)
#         op = int(input("Selecione una de las opciones: "))
#         if(op== 1):
#             print(tabulate(postProducto(),tablefmt="grid"))
#             input("Precione una tecla para continuar.....")
#         elif(op== 0):
#             break