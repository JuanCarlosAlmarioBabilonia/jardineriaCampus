import json
import requests
from tabulate import tabulate
import os
import re
import modules.getEstados as gE
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
                estado= input("Seleccione el estado del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gE.getAllName())]))
            if re.match(r'^[0-4]$', estado) is not None:  
                estado = int(estado)
                estado = gE.getAllName()[estado]
                pedido["estado"] = estado
            else:
                raise Exception("El estado del producto no cumple con el estándar establecido")
            
            if(not pedido.get("comentario")):
                comentario=input("Ingrese un comentario: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',comentario)is not None):
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
    pet=requests.post("http://172.16.103.37:5510", data=json.dumps(pedido))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE PEDIDOS
1.Guardar un pedido
0.Atras
              """)
        op = int(input("Selecione una de las opciones: "))
        if(op==1):
            print(tabulate(postPedido(),tablefmt="grid"))
            input("Precione una tecla para continuar.....")
        elif(op== 0):
            break