import json
import requests
from tabulate import tabulate
import os
import re
import modules.getPedido as gPed
def postPedido():
    pedido=dict()
    while True:
        try:
            if(not pedido.get("codigo_pedido")):
                codigo_pedido=input("Ingrese el codigo del pedido: ")
                if(re.match(r'^[0-9]+$',codigo_pedido)is not None):
                    codigo_pedido= int(codigo_pedido)
                    data=gPed.getPedidoCode(codigo_pedido)
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El codigo ya pertenece a un pedido")
                    else:
                        pedido["codigo_pedido"]=codigo_pedido
                else:
                    raise Exception("El codigo del cliente no cumple con el estandar establecido")
            if(not pedido.get("fecha_pedido")): 
                fecha_pedido=input("Ingrese la fecha del pedido: ")
            if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pedido)is not None):
                    pedido["fecha_pedido"]=fecha_pedido
            else:
                raise Exception("La fecha del pedido no cumple con el estandar establecido")
            
            if(not pedido.get("fecha_esperada")): 
                fecha_esperada=input("Ingrese la fecha esperada de entrega: ")
            if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_esperada)is not None):
                    pedido["fecha_esperada"]=fecha_esperada
            else:
                raise Exception("La fecha esperada de entrega no cumple con el estandar establecido")
            
            if(not pedido.get("fecha_entrega")): 
                fecha_entrega=input("Ingrese la fecha de entrega: ")
            if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_entrega)is not None):
                    pedido["fecha_entrega"]=fecha_entrega
            else:
                raise Exception("La fecha de entrega no cumple con el estandar establecido")
            
            if not pedido.get("estado"):
                estado= input("""Escriba su estado
1. Entregado
2. Pendiente
3. Rechazado
""")
            if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',estado)is not None): 
                print(tabulate(data, headers="keys",tablefmt="grid")) 
                pedido["estado"] = estado
            else:
                raise Exception("El estado del producto no cumple con el estándar establecido")
            
            if(not pedido.get("comentario")):
                comentario=input("Ingrese un comentario: ")
                if(re.match(r'^[^\n]+$', comentario) is not None):
                    pedido["comentario"]=comentario
                else:
                    raise Exception("El comentario del pedido no cumple con el estandar establecido") 

            if(not pedido.get("codigo_cliente")):
                codigo_cliente=input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]{2}$',codigo_cliente)is not None):
                    codigo_cliente= int(codigo_cliente)
                    pedido["codigo_cliente"]=codigo_cliente
                    break
                else:
                    raise Exception("El codigo del cliente no cumple con el estandar establecido")
        except Exception as error:        
            print(error)
    pet=requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(pedido))
    res=pet.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]
def deletePedido(id):
    data=gPed.getPedidoCode(id)
    if(len(data)):
        while True:
            try:
                print("""
¿DESEA ELIMINAR COMPLETAMENTE EL PEDIDO?
1. Si
2. No
               """)
                afirm = (input("Selecione una de las opciones: "))
                if(re.match(r'^[1-2]$', afirm)is not None):
                        afirm=int(afirm)
                        if (afirm==1):
                            pet=requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
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
            "message": "Pedido no encontrado",
            "id": id
        }]  
def updatePedido(id):
    data=gPed.getPedidoCode(id)
    if(len(data)):
            pedido=dict()
            while True:
                try:
                    if(not pedido.get("codigo_pedido")):
                        codigo_pedido=input("Ingrese el codigo del pedido: ")
                        if(re.match(r'^[0-9]+$',codigo_pedido)is not None):
                            codigo_pedido= int(codigo_pedido)
                            data=gPed.getPedidoCode(codigo_pedido)
                            if(data):
                                print(tabulate(data,tablefmt="grid"))
                                raise Exception("El codigo ya pertenece a un pedido")
                            else:
                                pedido["codigo_pedido"]=codigo_pedido
                        else:
                            raise Exception("El codigo del cliente no cumple con el estandar establecido")
                    if(not pedido.get("fecha_pedido")): 
                        fecha_pedido=input("Ingrese la fecha del pedido: ")
                        if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pedido)is not None):
                            pedido["fecha_pedido"]=fecha_pedido
                        else:
                            raise Exception("La fecha del pedido no cumple con el estandar establecido")
                    
                    if(not pedido.get("fecha_esperada")): 
                        fecha_esperada=input("Ingrese la fecha esperada de entrega: ")
                        if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_esperada)is not None):
                            pedido["fecha_esperada"]=fecha_esperada
                        else:
                            raise Exception("La fecha esperada de entrega no cumple con el estandar establecido")
                    
                    if(not pedido.get("fecha_entrega")): 
                        fecha_entrega=input("Ingrese la fecha de entrega: ")
                        if(re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_entrega)is not None):
                            pedido["fecha_entrega"]=fecha_entrega
                        else:
                            raise Exception("La fecha de entrega no cumple con el estandar establecido")
                    
                    if not pedido.get("estado"):
                        estado= input("""Escriba su estado
        1. Entregado
        2. Pendiente
        3. Rechazado
        """)
                    if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',estado)is not None): 
                        print(tabulate(data, headers="keys",tablefmt="grid")) 
                        pedido["estado"] = estado
                    else:
                        raise Exception("El estado del producto no cumple con el estándar establecido")
                    
                    if(not pedido.get("comentario")):
                        comentario=input("Ingrese un comentario: ")
                        if(re.match(r'^[^\n]+$', comentario) is not None):
                            pedido["comentario"]=comentario
                        else:
                            raise Exception("El comentario del pedido no cumple con el estandar establecido") 

                    if(not pedido.get("codigo_cliente")):
                        codigo_cliente=input("Ingrese el codigo del cliente: ")
                        if(re.match(r'^[0-9]{2}$',codigo_cliente)is not None):
                            codigo_cliente= int(codigo_cliente)
                            pedido["codigo_cliente"]=codigo_cliente
                            break
                        else:
                            raise Exception("El codigo del cliente no cumple con el estandar establecido")
                except Exception as error:        
                    print(error)
            pet=requests.put(f"http://154.38.171.54:5007/pedidos/{id}", data=json.dumps(pedido))
            res=pet.json()
            res["Mensaje"] = "Pedido Guardado"
            return [res]    
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE PEDIDOS
0. Atras
1. Guardar un pedido
2. Eliminar un pedido
3. Actualizar un pedido
              """)
        op = (input("Selecione una de las opciones: "))
        if(re.match(r'^[0-3]$', op)is not None):
            op=int(op)
        if(op==1):
            print(tabulate(postPedido(),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op==2):
            idProducto=int(input("Ingrese el id del pedido que desea eliminar:"))
            print(tabulate(deletePedido(idProducto),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op==3):
            idProducto=int(input("Ingrese el id del pedido que desea actualizar:"))
            print(tabulate(updatePedido(idProducto),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op== 0):
            break