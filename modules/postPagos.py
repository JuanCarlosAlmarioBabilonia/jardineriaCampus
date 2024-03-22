import json
import requests
from tabulate import tabulate
import os
import re
import modules.getClientes as gC
import modules.getPago as gPa
# import modules.getPago as Gpag
def postPagos():
    pagos=dict()
    while True:
        try:
            if(not pagos.get("codigo_cliente")):
                codigo_cliente=input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]+$',codigo_cliente)is not None):
                    codigo_cliente= int(codigo_cliente)
                    data=gC.getClienteCodigo(codigo_cliente)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo ya pertenece a un cliente")
                    else:
                        pagos["codigo_cliente"]=codigo_cliente
                else:
                    raise Exception("El codigo del cliente no cumple con el estandar establecido")
        
            if (not pagos.get("forma_pago")):
                forma_pago= input("""Ingrese su forma de pago
1. Paypal
2. Transferencia
3. Cheque
""")
            if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',forma_pago)is not None):
                pagos["forma_pago"] = forma_pago
            else:
                raise Exception("La forma de pago no cumple con el estándar establecido")

            if(not pagos.get("id_transaccion")): #no se por que cuando pongo un valor que no es valido, en vez de salir una cola vez, sale una lista infinita de texto diciendo que quedo mal
                id_transaccion=input("Ingrese su ID de transaccion: ")
            if(re.match(r'^[a-z]{2}-[a-z]{3}-\d{6}$',id_transaccion)is not None):
                    pagos["id_transaccion"]=id_transaccion
            else:
                raise Exception("El ID de transaccion no cumple con el estandar establecido")
            
            if(not pagos.get("fecha_pago")): 
                fecha_pago=input("Ingrese la fecha de pago: ")
            if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pago)is not None):
                    pagos["fecha_pago"]=fecha_pago
            else:
                raise Exception("La fecha de pago no cumple con el estandar establecido")
            
            if(not pagos.get("total")):
                total=input("Ingrese el total: ")
                if(re.match(r'^[0-9]{4,5}$',total)is not None):
                    total= int(total)
                    pagos["total"]=total
                    break
                else:
                    raise Exception("Su limite de credito no cumple con el estandar establecido")
        
        except Exception as error:        
            print(error)
    pet=requests.post("http://154.38.171.54:5006/pagos", data=json.dumps(pagos))
    res=pet.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]
def deletePagos(id):
    data=gPa.getPagoCodigo(id)
    if(len(data)):
        while True:
            try:
                print("""
¿DESEA ELIMINAR COMPLETAMENTE EL PAGO?
1. Si
2. No
               """)
                afirm = (input("Selecione una de las opciones: "))
                if(re.match(r'^[1-2]$', afirm)is not None):
                        afirm=int(afirm)
                        if (afirm==1):
                            pet=requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
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
            "message": "Pago no encontrado",
            "id": id
        }]  
def updatePagos(id):
    data=gPa.getPagoCodigo(id)
    if(len(data)):
        pagos=dict()
        while True:
            try:
                if(not pagos.get("codigo_cliente")):
                    codigo_cliente=input("Ingrese el codigo del cliente: ")
                    if(re.match(r'^[0-9]+$',codigo_cliente)is not None):
                        codigo_cliente= int(codigo_cliente)
                        data=gC.getClienteCodigo(codigo_cliente)
                        if(data):
                            print(tabulate(data,tablefmt="grid"))
                            raise Exception("El codigo ya pertenece a un cliente")
                        else:
                            pagos["codigo_cliente"]=codigo_cliente
                    else:
                        raise Exception("El codigo del cliente no cumple con el estandar establecido")
            
                if (not pagos.get("forma_pago")):
                    forma_pago= input("""Escriba su forma de pago
1. Paypal
2. Transferencia
3. Cheque
    """)
                if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',forma_pago)is not None):
                    pagos["forma_pago"] = forma_pago
                else:
                    raise Exception("La forma de pago no cumple con el estándar establecido")

                if(not pagos.get("id_transaccion")): #no se por que cuando pongo un valor que no es valido, en vez de salir una cola vez, sale una lista infinita de texto diciendo que quedo mal
                    id_transaccion=input("Ingrese su ID de transaccion: ")
                if(re.match(r'^[a-z]{2}-[a-z]{3}-\d{6}$',id_transaccion)is not None):
                        pagos["id_transaccion"]=id_transaccion
                else:
                    raise Exception("El ID de transaccion no cumple con el estandar establecido")
                
                if(not pagos.get("fecha_pago")): 
                    fecha_pago=input("Ingrese la fecha de pago: ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pago)is not None):
                        pagos["fecha_pago"]=fecha_pago
                else:
                    raise Exception("La fecha de pago no cumple con el estandar establecido")
                
                if(not pagos.get("total")):
                    total=input("Ingrese el total: ")
                    if(re.match(r'^[0-9]{4,5}$',total)is not None):
                        total= int(total)
                        pagos["total"]=total
                        break
                    else:
                        raise Exception("Su limite de credito no cumple con el estandar establecido")         
            except Exception as error:        
                print(error)
        pet=requests.put(f"http://154.38.171.54:5006/pagos/{id}", data=json.dumps(pagos))
        res=pet.json()
        res["Mensaje"] = "Pago Guardado"
        return [res]
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE PAGOS
0. Atras
1. Guardar un pago
2. Eliminar un pago
3. Actualizar un pago
              """)
        op = (input("Selecione una de las opciones: "))
        if(re.match(r'^[0-3]$', op)is not None):
            op=int(op)
        if(op==1):
            print(tabulate(postPagos(),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op==2):
            idProducto=int(input("Ingrese el id del pago que desea eliminar: "))
            print(tabulate(deletePagos(idProducto),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op==3):
            idProducto=int(input("Ingrese el id del pago que desea actualizar:"))
            print(tabulate(updatePagos(idProducto),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op== 0):
            break