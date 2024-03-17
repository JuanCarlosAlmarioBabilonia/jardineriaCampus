import json
import requests
from tabulate import tabulate
import os
import re
import modules.getClientes as gC
import modules.getCodeEmp as gCem
def postCliente():
    cliente=dict()
    while True:
        try:
            # corregir porque no me deja hacer el filtro para que solo puedan ingresarse codigos no existentes
            if(not cliente.get("codigo_cliente")):
                codigo=input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]{2}$',codigo)is not None):
                    codigo= int(codigo)
                    cliente["codigo_producto"]=codigo
                else:
                    raise Exception("El codigo del cliente no cumple con el estandar establecido")
                
            if(not cliente.get("nombre_cliente")):
                nombre_cliente=input("Ingrese el nombre del cliente: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre_cliente)is not None):
                    cliente["nombre_cliente"]=nombre_cliente
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")

            if(not cliente.get("nombre_contacto")):
                nombre_contacto=input("Ingrese su nombre: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre_contacto)is not None):
                    cliente["nombre_contacto"]=nombre_contacto
                else:
                    raise Exception("Su nombre no cumple con el estandar establecido") 

            if(not cliente.get("apellido_contacto")):
                apellido_contacto=input("Ingrese sus apellidos: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',apellido_contacto)is not None):
                    cliente["apellido_contacto"]=apellido_contacto
                else:
                    raise Exception("Sus apellidos no cumplen con el estandar establecido")   

            if(not cliente.get("telefono")):
                telefono=input("Ingrese su telefono: ")
                if(re.match(r'^[0-9]{9,11}$',telefono)is not None):
                    telefono= int(telefono)
                    cliente["telefono"]=telefono
                else:
                    raise Exception("Su telefono no cumple con el estandar establecido")  

            if(not cliente.get("fax")):
                fax=input("Ingrese su fax: ")
                if(re.match(r'^[0-9]{9,11}$',fax)is not None):
                    fax= int(fax)
                    cliente["fax"]=fax
                else:
                    raise Exception("Su fax no cumple con el estandar establecido")   

            if(not cliente.get("linea_direccion1")):
                linea_direccion1=input("Ingrese su direccion principal: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',linea_direccion1)is not None):
                    cliente["linea_direccion1"]=linea_direccion1
                else:
                    raise Exception("Su linea de direccion principal no cumple con el estandar establecido")   
                
            if(not cliente.get("linea_direccion2")):
                linea_direccion2=input("Ingrese su direccion principal: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',linea_direccion2)is not None):
                    cliente["linea_direccion2"]=linea_direccion2
            
            if(not cliente.get("ciudad")):
                ciudad=input("Ingrese su ciudad: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',ciudad)is not None):
                    cliente["ciudad"]=ciudad
                else:
                    raise Exception("Su ciudad no cumple con el estandar establecido")  
                
            if(not cliente.get("region")):
                region=input("Ingrese su region: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',region)is not None):
                    cliente["region"]=region
                else:
                    raise Exception("Su region no cumple con el estandar establecido")  
            
            if(not cliente.get("pais")):
                pais=input("Ingrese su pais: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',pais)is not None):
                    cliente["pais"]=pais
                else:
                    raise Exception("Su pais no cumple con el estandar establecido")  
            
            if(not cliente.get("codigo_postal")):
                codigo_postal=input("Ingrese su codigo postal: ")
                if(re.match(r'^[0-9]{5}$',codigo_postal)is not None):
                    codigo_postal= int(codigo_postal)
                    cliente["codigo_postal"]=codigo_postal
                else:
                    raise Exception("Su codigo postal no cumple con el estandar establecido")  
                
            if(not cliente.get("codigo_empleado_rep_ventas")):
                codigo_empleado_rep_ventas=input("Seleccione el codigo de su Representante de Ventas:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gCem.getAllCoEmp())]))
                if(re.match(r'^[0-9]$',codigo_empleado_rep_ventas)is not None):
                    codigo_empleado_rep_ventas= int(codigo_empleado_rep_ventas)
                    codigo_empleado_rep_ventas = gCem.getAllCoEmp()[codigo_empleado_rep_ventas]
                    cliente["codigo_empleado_rep_ventas"]=codigo_empleado_rep_ventas
                else:
                    raise Exception("El codigo de su Representante no cumple con el estandar establecido")  
                
            
            if(not cliente.get("limite_credito")):
                limite_credito=input("Ingrese su limite de credito: ")
                if(re.match(r'^[0-9]{4,5}$',limite_credito)is not None):
                    limite_credito= int(limite_credito)
                    cliente["limite_credito"]=limite_credito
                    break
                else:
                    raise Exception("Su limite de credito no cumple con el estandar establecido")  
        except Exception as error:
            print(error)
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