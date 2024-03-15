import json
import requests
from tabulate import tabulate
import os
def postEmpleados():
    empleado={
        "codigo_empleado": int(input("Ingrese su codigo del empleado: ")),
        "nombre": input("Ingrese el nombre: "),
        "apellido1": input("Ingrese su primer apellido: "),
        "apellido2": input("Ingrese su segundo apellido: "),
        "extension": int(input("Ingrese su extension: ")),
        "email": input("Ingrese su email: "),
        "codigo_oficina": input("Ingrese su codigo de oficina: "),
        "codigo_jefe": int(input("Ingrese su codigo de jefe: ")),
        "puesto": input("Ingrese su puesto: ")
    }
    pet=requests.post("http://192.168.20.37:5507", data=json.dumps(empleado))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE EMPLEADOS
1.Guardar un empleado
0.Atras
              """)
        op = int(input("Selecione una de las opciones: "))
        if(op==1):
            print(tabulate(postEmpleados(),tablefmt="grid"))
            input("Precione una tecla para continuar.....")
        elif(op== 0):
            break