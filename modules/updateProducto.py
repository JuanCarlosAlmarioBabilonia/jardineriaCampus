import json
import requests
from tabulate import tabulate
import modules.getProducto as gP
import modules.getGamas as gG
import os
import re

def updateProductoNombre(id):
    while True:
        if(id != None):
            producto=gP.getProductCodigo2(id)
            if(producto):
                print(tabulate(producto, headers="keys", tablefmt="grid"))
                op=int(input("""
¿Desea actualizar el nombre del producto?
1. Si
2. No
"""))
                if(op):
                    headers={'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["nombre"]=input("Ingrese el nuevo nombre del producto: ")
                    pet=requests.put(f"http://154.38.171.54:5008/productos/{producto[0].get('id')}", headers=headers, data=json.dumps(producto[0]))
                    input("Nombre del producto = ACTUALIZADO")
                    data=pet.json()
                    return data
                else:
                    id = None
            else:
                print("Este producto no existe")
                id = None
        else:
            id = input("Ingrese el codigo del producto que desea actualizar")

def updateGamaProducto(id):
    while True:
        if(id != None):
            producto=gP.getProductCodigo2(id)
            if(producto):
                print(tabulate(producto, headers="keys", tablefmt="grid"))
                op=int(input("""
¿Desea actualizar la gama del producto?
1. Si
2. No
"""))
                if(op):
                    headers={'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["gama"]=input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
                    pet=requests.put(f"http://154.38.171.54:5008/productos/{producto[0].get('id')}", headers=headers, data=json.dumps(producto[0]))
                    input("gama del producto = ACTUALIZADO")
                    data=pet.json()
                    return [data[0]]
                else:
                    id = None
            else:
                print("Este producto no existe")
                id = None
        else:
            id = input("Ingrese el codigo del producto que desea actualizar")

def menuActualizacionProducto():
    while True:
        os.system("clear")
        print("""
MENU DE ACTUALIZACION
1. Actualizar el codigo del producto
2. Actualizar el nombre del producto
3. Actualizar la gama del producto
4. Actualizar las dimensiones
5. Actualizar el proveedor del producto
6. Actualizar la descripcion del producto
7. Actualizar la cantidad en stock del producto
8. Actualizar el precio de venta del producto
9. Actualizar el precio del proveedor del producto
10. Actualizar todos los datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-9]$', op)is not None):
            op=int(op)
        if(op==2):
            codigo=int(input("Ingrese el code"))
            if(re.match(r'^[0-9]$',codigo)is not None):
                updateProductoNombre(codigo)