import json
import requests
from tabulate import tabulate
import os
def postCliente():
    cliente={
        "codigo_cliente": input("Ingrese el codigo: "),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese su nombre: "),
        "apellido_contacto": input("Ingrese su apellido: "),
        "telefono": int(input("Ingrese su telefono: ")),
        "fax": int(input("Ingrese su fax: ")),
        "linea_direccion1": input("Ingrese su direccion principal: "),
        "linea_direccion2":input("Ingrese su direccion secundaria: "),
        "ciudad": input("Ingrese su ciudad: "),
        "region": input("Ingrese su region: "),
        "pais": input("Ingrese su pais: "),
        "codigo_postal": int(input("Ingrese su codigo postal: ")),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo de su Rep. de ventas: ")),
        "limite_credito": int(input("Ingrese su limite de credito: "))
    }
    pet=requests.post("http://192.168.20.37:5506", data=json.dumps(cliente))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE CLIENTES
1.Guardar un cliente
0.Atras
              """)
        op = int(input("Selecione una de las opciones: "))
        if(op==1):
            print(tabulate(postCliente(),tablefmt="grid"))
            input("Precione una tecla para continuar.....")
        elif(op== 0):
            break