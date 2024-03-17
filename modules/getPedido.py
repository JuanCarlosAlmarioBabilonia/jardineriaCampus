import requests
import os
from tabulate import tabulate
from datetime import datetime
def getAllDataPed():
    pet=requests.get("http://192.168.20.37:5510")
    data=pet.json()
    return data
def getEstadoPedido(): 
    estadoPedido=[]
    estadoPedidoVistos=set()
    for val in getAllDataPed():
        estadoDePedidos=val.get("estado")
        if estadoDePedidos not in estadoPedidoVistos:
            estadoPedido.append({
                "Estados del Pedido": val.get("estado")
            })
            estadoPedidoVistos.add(estadoDePedidos)
    return estadoPedido
def getAllPedidosEntregadosDespuesDeTiempo():
    pedidosEntregados=[]
    for val in getAllDataPed():
        if(val.get("estado")=="Entregado") and (val.get("fecha_entrega")==None):
            val["fecha_entrega"]=val.get("fecha_esperada")
        if(val.get("estado")=="Entregado"):
            date_1="/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2="/".join(val.get("fecha_esperada").split("-")[::-1])
            start=datetime.strptime(date_1,"%d/%m/%Y")
            end=datetime.strptime(date_2,"%d/%m/%Y")
            dif=end.date()-start.date()
            if(dif.days<0):
                pedidosEntregados.append({
                    "Codigo del pedido":val.get("codigo_pedido"),
                    "Codigo del cliente":val.get("codigo_cliente"),
                    "Fecha esperada":val.get("fecha_esperada"),
                    "Fecha de entrega":val.get("fecha_entrega")
                })
    return pedidosEntregados
def getAllPedidosRechazados():
    pedidosRechazados=[]
    for val in getAllDataPed():
        if(val.get("fecha_pedido")>=("2009-01-01") and (val.get("fecha_pedido")<=("2009-12-31")) and (val.get("estado")==("Rechazado"))):
            pedidosRechazados.append({
                "Codigo del pedido":val.get("codigo_pedido"),
                "Fecha del pedido":val.get("fecha_pedido"), 
                "Fecha esperada":val.get("fecha_esperada"), 
                "Fecha de entrega":val.get("fecha_entrega"), 
                "Estado del pedido":val.get("estado"), 
                "Comentario":val.get("comentario"), 
                "Codigo del cliente":val.get("codigo_cliente")
            })
    return pedidosRechazados
def getAllPedidosEntregadoAntesDeTiempo():
    pedidosAntes=[]
    for val in getAllDataPed():
        if(val.get("estado")=="Entregado") and (val.get("fecha_entrega")==None):
            val["fecha_entrega"]=val.get("fecha_esperada")
        if(val.get("estado")=="Entregado"):
            date_1="/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2="/".join(val.get("fecha_esperada").split("-")[::-1])
            start=datetime.strptime(date_1,"%d/%m/%Y")
            end=datetime.strptime(date_2,"%d/%m/%Y")
            dif=end.date()-start.date()
            if(dif.days>=2):
                pedidosAntes.append({
                    "Codigo del pedido":val.get("codigo_pedido"),
                    "Codigo del cliente":val.get("codigo_cliente"),
                    "Fecha esperada":val.get("fecha_esperada"),
                    "Fecha de entrega":val.get("fecha_entrega")
                })
    return pedidosAntes
def getAllPedidosEntEnEnero():
    pedidosEnero=[]
    for val in getAllDataPed():
        fecha=val.get("fecha_entrega")
        if fecha:
            date_1="/".join(val.get("fecha_entrega").split("-")[::-1])
            start=datetime.strptime(date_1,"%d/%m/%Y")
            if(start.month==1) and val.get("estado")=="Entregado":
                pedidosEnero.append({
                    "Codigo del pedido":val.get("codigo_pedido"),
                    "Codigo del cliente":val.get("codigo_cliente"),
                    "Fecha de entrega":val.get("fecha_entrega"),
                    "Estado del pedido":val.get("estado")
                })
    return pedidosEnero
def menu():
    while True:
     print("""
REPORTES DE LOS PEDIDOS
0. Regresar al menu principal
1. Obtener los estados por los que puede pasar un pedido
2. Obtener todos los pedidos entregados despues de tiempo
3. Obtener todos los pedidos rechazados
4. Obtener todos los pedidos entregados con 2 o mas dias de anticipacion
5. Obtener todos los pedidos entregados en el mes de Enero de cualquier año
""")
     op=int(input("Seleccione una de las opciones: "))
     if(op==1):
        print(tabulate(getEstadoPedido(),headers="keys",tablefmt="grid"))
     elif(op==2):
        print(tabulate(getAllPedidosEntregadosDespuesDeTiempo(),headers="keys",tablefmt="grid"))
     elif(op==3):
        print(tabulate(getAllPedidosRechazados(),headers="keys",tablefmt="grid"))
     elif(op==4):
        print(tabulate(getAllPedidosEntregadoAntesDeTiempo(),headers="keys",tablefmt="grid"))
     elif(op==5):
        print(tabulate(getAllPedidosEntEnEnero(),headers="keys",tablefmt="grid"))
     elif (op==0):
        break
     