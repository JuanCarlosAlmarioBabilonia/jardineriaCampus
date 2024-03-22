import json
import requests
from tabulate import tabulate
import os
import re
import modules.getClientes as gC
def postCliente():
    cliente=dict()
    while True:
        try:
            if(not cliente.get("codigo_cliente")):
                codigo_cliente=input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]+$',codigo_cliente)is not None):
                    codigo_cliente= int(codigo_cliente)
                    data=gC.getClienteCodigo(codigo_cliente)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo ya pertenece a un cliente")
                    else:
                        cliente["codigo_cliente"]=codigo_cliente
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
                if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion1)is not None):
                    cliente["linea_direccion1"]=linea_direccion1
                else:
                    raise Exception("Su linea de direccion principal no cumple con el estandar establecido")   
                
            if(not cliente.get("linea_direccion2")):
                linea_direccion2=input("Ingrese su direccion principal: ")
                if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion2)is not None):
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
                
            
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigo_empleado_rep_ventas= (input("""Ingrese su representante (codigo)
1. 5
2. 8
3. 9
4. 11
5. 12
6. 18
7. 19
8. 22
9. 30
10. 31
"""))
            if(re.match(r'^[0-9]{1,2}$',codigo_empleado_rep_ventas)is not None): 
                codigo_empleado_rep_ventas=int(codigo_empleado_rep_ventas)
                cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
            else:
                raise Exception("El estado del producto no cumple con el estándar establecido") 
                           
            if(not cliente.get("limite_credito")):
                limite_credito=input("Ingrese su limite de credito: ")
                if(re.match(r'^[0-9]{4,5}$',limite_credito)is not None):
                    limite_credito= float(limite_credito)
                    cliente["limite_credito"]=limite_credito
                    break
                else:
                    raise Exception("Su limite de credito no cumple con el estandar establecido")  
        except Exception as error:
            print(error)
    pet=requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(cliente))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def deleteCliente(id):
    data=gC.getClienteCodigo(id)
    if(len(data)):
        while True:
            try:
                print("""
¿DESEA ELIMINAR COMPLETAMENTE EL CLIENTE?
1. Si
2. No
               """)
                afirm = input("Selecione una de las opciones: ")
                if(re.match(r'^[1-2]$', afirm)is not None):
                        afirm=int(afirm)
                        if (afirm==1):
                            pet=requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
                            if(pet.status_code==204):
                                return print("El producto ha sido eliminado satisfactoriamente")
                            break
                        else:
                            return print("Eliminacion cancelada")
                        
                else:
                    raise Exception("El dato ingresado no esta comprendido entre los estandares solicitados")
            except Exception as error:
                print(error)
    else:
        return[{
            "message": "Cliente no encontrado",
            "id": id
        }]   
def updateCliente(id):
    data=gC.getClienteCodigo(id)
    if(len(data)):
            cliente=dict()
            while True:
                try:
                    if(not cliente.get("codigo_cliente")):
                        codigo_cliente=input("Ingrese el codigo del cliente: ")
                        if(re.match(r'^[0-9]+$',codigo_cliente)is not None):
                            codigo_cliente= int(codigo_cliente)
                            data=gC.getClienteCodigo2(codigo_cliente)
                            if(data):
                                print(tabulate(data,tablefmt="grid"))
                                raise Exception("El codigo ya pertenece a un cliente")
                            else:
                                cliente["codigo_cliente"]=codigo_cliente
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
                        if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion1)is not None):
                            cliente["linea_direccion1"]=linea_direccion1
                        else:
                            raise Exception("Su linea de direccion principal no cumple con el estandar establecido")   
                    
                    if(not cliente.get("linea_direccion2")):
                        linea_direccion2=input("Ingrese su direccion secundaria: ")
                        if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion2)is not None):
                            cliente["linea_direccion2"]=linea_direccion2
                        else:
                            raise Exception("Su linea de direccion secundaria no cumple con el estandar establecido")   
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
                    
                    if not cliente.get("codigo_empleado_rep_ventas"):
                        codigo_empleado_rep_ventas= input("""Escriba su representante (codigo)
1. 5
2. 8
3. 9
4. 11
5. 12
6. 18
7. 19
8. 22
9. 30
10. 31
""")
                    if(re.match(r'^[0-9]{1,2}$',codigo_empleado_rep_ventas)is not None): 
                        codigo_empleado_rep_ventas=int(codigo_empleado_rep_ventas)
                        cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
                    else:
                        raise Exception("El codigo no cumple con el estándar establecido") 
                                
                    if(not cliente.get("limite_credito")):
                        limite_credito=input("Ingrese su limite de credito: ")
                        if(re.match(r'^[0-9]{4,5}$',limite_credito)is not None):
                            limite_credito= float(limite_credito)
                            cliente["limite_credito"]=limite_credito
                            break
                        else:
                            raise Exception("Su limite de credito no cumple con el estandar establecido")  
                                    
                    if(not cliente.get("limite_credito")):
                        limite_credito=input("Ingrese su limite de credito: ")
                        if(re.match(r'^[0-9]{4,5}$',limite_credito)is not None):
                            limite_credito= float(limite_credito)
                            cliente["limite_credito"]=limite_credito
                            break
                        else:
                            raise Exception("Su limite de credito no cumple con el estandar establecido")  
                except Exception as error:
                    print(error)  
            pet=requests.put(f"http://154.38.171.54:5001/cliente/{id}", data=json.dumps(cliente))
            res=pet.json()
            res["Mensaje"] = "Cliente Guardado"
            return [res]
    else:
        return[{
            "message": "Cliente no encontrado",
            "id": id
        }]   
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE CLIENTES
0. Atras
1. Guardar un cliente
2. Eliminar un cliente
3. Actualizar un cliente
              """)
        op = (input("Selecione una de las opciones: "))
        if(re.match(r'^[0-3]$', op)is not None):
            op=int(op)
        if(op==1):
            print(tabulate(postCliente(),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op==2):
            idProducto=int(input("Ingrese el id del cliente que desea eliminar:"))
            print(tabulate(deleteCliente(idProducto),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op==3):
            idProducto=int(input("Ingrese el id del cliente que desea actualizar:"))
            print(tabulate(updateCliente(idProducto),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op== 0):
            break