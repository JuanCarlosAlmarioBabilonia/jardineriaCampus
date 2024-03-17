import json
import requests
from tabulate import tabulate
import os
import modules.getFormasPago as fPago
def postPagos():
    pagos={
        "codigo_cliente": input("Ingrese el codigo del cliente: "),
        "forma_pago": fPago.getAllTipoP()[int(input("Selecione la forma de pago:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(fPago.getAllTipoP())])))],
        "id_transaccion": input("Ingrese su id de transaccion: "),
        "fecha_pago":input("Ingrese su fecha de pago (año-mes-dia): "),
        "total": int(input("Ingrese el total: "))
    }
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