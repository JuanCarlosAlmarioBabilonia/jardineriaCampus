import json
import requests
from tabulate import tabulate
import os
import modules.getFormasPago as fPago
import re
import modules.getClientes as gC
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
                forma_pago= input("Seleccione la forma de pago:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(fPago.getAllTipoP())]))
            if re.match(r'^[0-4]$', forma_pago) is not None:  
                forma_pago = int(forma_pago)
                forma_pago = fPago.getAllTipoP()[forma_pago]
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
    pet=requests.post("http://192.168.20.37:5508", data=json.dumps(pagos))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE PAGOS
1.Guardar un pago
0.Atras
              """)
        op = int(input("Selecione una de las opciones: "))
        if(op==1):
            print(tabulate(postPagos(),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op== 0):
            break