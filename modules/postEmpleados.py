import json
import requests
from tabulate import tabulate
import os
import modules.getPuestos as gPu
import re
import modules.getCodeOficina as gCof
def postEmpleados():
    empleado=dict()
    while True:
        try:
            # corregir porque no me deja hacer el filtro para que solo puedan ingresarse codigos no existentes
            if(not empleado.get("codigo_empleado")):
                codigo_empleado=input("Ingrese el codigo del empleado: ")
                if(re.match(r'^[0-9]{2}$',codigo_empleado)is not None):
                    codigo_empleado= int(codigo_empleado)
                    empleado["codigo_empleado"]=codigo_empleado
                else:
                    raise Exception("El codigo del cliente no cumple con el estandar establecido")
                
            if(not empleado.get("nombre")):
                nombre=input("Ingrese su nombre: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre)is not None):
                    empleado["nombre"]=nombre
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")
            
            if(not empleado.get("apellido1")):
                apellido1=input("Ingrese su primer apellido: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',apellido1)is not None):
                    empleado["apellido1"]=apellido1
                else:
                    raise Exception("Su primer apellido no cumple con el estandar establecido") 

            if(not empleado.get("apellido2")):
                apellido2=input("Ingrese su segundo apellido: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',apellido2)is not None):
                    empleado["apellido2"]=apellido2
                else:
                    raise Exception("Su segundo apellido no cumple con el estandar establecido") 
            
            if(not empleado.get("email")):
                email=input("Ingrese su email: ")
                if(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email)is not None):
                    empleado["email"]=email
                else:
                    raise Exception("Su email no cumple con el estandar establecido") 
                
            if not empleado.get("codigo_oficina"):
                codigo_oficina= input("Seleccione el codigo de la oficina:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gCof.getAllNameOf())]))
            if re.match(r'^[0-8]$', codigo_oficina) is not None:  
                codigo_oficina = int(codigo_oficina)
                codigo_oficina = gCof.getAllNameOf()[codigo_oficina]
                empleado["codigo_oficina"] = codigo_oficina
            else:
                raise Exception("El codigo de oficina no cumple con el estándar establecido")
            
            if(not empleado.get("codigo_jefe")):
                codigo_jefe=input("Ingrese el codigo de jefe: ")
                if(re.match(r'^[0-9]{2}$',codigo_jefe)is not None):
                    codigo_jefe= int(codigo_jefe)
                    empleado["codigo_jefe"]=codigo_jefe
                else:
                    raise Exception("El codigo del cliente no cumple con el estandar establecido")
            
            if not empleado.get("puesto"):
                puesto= input("Seleccione su puesto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gPu.getAllTipoPu())]))
            if re.match(r'^[0-4]$', puesto) is not None:  
                puesto = int(puesto)
                puesto = gPu.getAllTipoPu()[puesto]
                empleado["puesto"] = puesto
                break
            else:
                raise Exception("El puesto no cumple con el estándar establecido")
                 
        except Exception as error:
            print(error)
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