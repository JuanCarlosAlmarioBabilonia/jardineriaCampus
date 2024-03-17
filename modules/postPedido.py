import json
import requests
from tabulate import tabulate
import os
import modules.getEstados as es
def postPedido():
    pedido={
        "codigo_pedido": int(input("Ingrese el codigo del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha del pedido (año-mes-dia): "),
        "fecha_esperada": input("Ingrese la fecha esperada del pedido (año-mes-dia): "),
        "fecha_entrega": input("Ingrese la fecha de entrega del pedido(año-mes-dia): "),
        "estado": es.getAllName()[int(input("Selecione el estado:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(es.getAllName())])))],
        "comentario": input("Ingrese un comentario: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
    }
    pet=requests.post("http://192.168.20.37:5510", data=json.dumps(pedido))
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