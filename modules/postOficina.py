import json
import requests
from tabulate import tabulate
import os
def postOficina():
    oficina={
        "codigo_oficina": input("Ingrese su codigo de oficina: "),
        "ciudad": input("Ingrese su ciudad: "),
        "pais": input("Ingrese su pais: "),
        "region": input("Ingrese su region: "),
        "codigo_postal": input("Ingrese su codigo postal (oficina): "),
        "telefono": input("Ingrese su telefono (oficina): "),
        "linea_direccion1": input("Ingrese su direccion principal de oficina: "),
        "linea_direccion2": input("Ingrese su direccion secundaria de oficina: ")
    }
    pet=requests.post("http://172.16.100.133:5509", data=json.dumps(oficina))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE OFICINAS
1.Guardar una oficina
0.Atras
              """)
        op = int(input("Selecione una de las opciones: "))
        if(op==1):
            print(tabulate(postOficina(),tablefmt="grid"))
            input("Precione una tecla para continuar.....")
        elif(op== 0):
            break