import json
import requests
from tabulate import tabulate
import os
import modules.getPuestos as gPu
import modules.getEmpleados as gEm
import re
import modules.getCodeOficina as gCof
def postEmpleados():
    empleado=dict()
    while True:
        try:
            # corregir porque no me deja hacer el filtro para que solo puedan ingresarse codigos no existentes
            if(not empleado.get("codigo_empleado")):
                codigo_empleado=input("Ingrese el codigo del empleado: ")
                if(re.match(r'^[0-9]+$',codigo_empleado)is not None):
                    codigo_empleado= int(codigo_empleado)
                    data=gEm.getAllCodeEmp(codigo_empleado)
                    if (data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo ya pertenece a un cliente")
                    else:    
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
            if re.match(r'^[0-9]{2}$', codigo_oficina) is not None:  
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
                puesto= input("""Ingrese su puesto
1. Subdirector Marketing
2. Secretaria
3. Director General
4. Representante Ventas""")
            if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',puesto)is not None):
                print(tabulate(data, headers="keys",tablefmt="grid"))
                empleado["puesto"]=puesto
                break
            else:
                raise Exception("El puesto no cumple con el estándar establecido")                 
        except Exception as error:
            print(error)
    pet=requests.post("http://154.38.171.54:5003/empleados", data=json.dumps(empleado))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def deleteEmpleado(id):
    data=gEm.getAllCodeEmp(id)
    if(len(data)):
        while True:
            try:
                print("""
¿DESEA ELIMINAR COMPLETAMENTE EL EMPLEADO?
1. Si
2. No
               """)
                afirm = (input("Selecione una de las opciones: "))
                if(re.match(r'^[1-2]$', afirm)is not None):
                        afirm=int(afirm)
                        if (afirm==1):
                            pet=requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
                            if(pet.status_code==204):
                                return[{"Mensaje": "El producto ha sido eliminado satisfactoriamente"}]
                            break
                        else:
                            return[{"Mensaje": "Eliminacion cancelada"}]
                        
                else:
                    raise Exception("El dato ingresado no esta comprendido entre los estandares solicitados")
            except Exception as error:
                print(error)
    else:
        return[{
            "message": "Producto no encontrado",
            "id": id
        }]  
def updateEmpleado(id):
    data=gEm.getAllCodeEmp(id)
    if(len(data)):
        empleado=dict()
        while True:
            try:
                if(not empleado.get("codigo_empleado")):
                    codigo_empleado=input("Ingrese el codigo del empleado: ")
                    if(re.match(r'^[0-9]+$',codigo_empleado)is not None):
                        codigo_empleado= int(codigo_empleado)
                        data=gEm.getAllCodeEmp(codigo_empleado)
                        if (data):
                            print(tabulate(data,tablefmt="grid"))
                            raise Exception("El codigo ya pertenece a un cliente")
                        else:    
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
                    puesto= input("""Ingrese su puesto
1. Subdirector Marketing
2. Secretaria
3. Director General
4. Representante Ventas""")
                if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',puesto)is not None):
                    print(tabulate(data, headers="keys",tablefmt="grid"))
                    empleado["puesto"]=puesto
                    break
                else:
                    raise Exception("El puesto no cumple con el estándar establecido")                 
            except Exception as error:
                print(error)
    pet=requests.put(f"http://154.38.171.54:5003/empleados/{id}", data=json.dumps(empleado))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE EMPLEADOS
0. Atras
1. Guardar un empleado
2. Eliminar un empleado
3. Actualizar un empleado
              """)
        op = (input("Selecione una de las opciones: "))
        if(re.match(r'^[0-3]$', op)is not None):
            op=int(op)
        if(op==1):
            print(tabulate(postEmpleados(),tablefmt="grid"))
            input("Precione una tecla para continuar.....")
        elif(op==2):
            idProducto=(input("Ingrese el id del empleado que desea eliminar:"))
            print(tabulate(deleteEmpleado(idProducto),tablefmt="grid"))
            input("...")
        elif(op==3):
            idProducto=(input("Ingrese el id del empleado que desea actualizar:"))
            print(tabulate(updateEmpleado(idProducto),tablefmt="grid"))
            input("...")
        elif(op== 0):
            break