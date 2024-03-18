import requests
import os
from tabulate import tabulate
def getAllDataOf():
    pet=requests.get("http://172.16.103.37:5509")
    data=pet.json()
    return data
def getOficinaCodigo(codigo):
    for val in getAllDataOf():
        if(val.get("codigo_oficina") == codigo):
            return [val]
def getAllCodigoCiudad():
    codigoCiudad=[]
    for val in getAllDataOf():
        codigoCiudad.append({
            "Codigo de la oficina":val.get("codigo_oficina"),
            "Ciudad":val.get("ciudad")
        })
    return codigoCiudad
def getAllCiudadTelefono(pais):
    ciudadTelefono=[]
    for val in getAllDataOf():
        if (val.get("pais")==pais):
            ciudadTelefono.append({
                "Codigo de la oficina":val.get("codigo_oficina"),
                "Telefono de la oficina":val.get("telefono"),
                "Ciudad":val.get("ciudad"),
                "Pais":val.get("pais")
            })
    return ciudadTelefono
def getAllDirecciones():
    direccion=[]
    for val in getAllDataOf():
        direccion.append({
                "Codigo de la oficina":val.get("codigo_oficina"),
                "Ciudad":val.get("ciudad"),
                "Pais":val.get("pais"),
                "Region":val.get("region"),
                "Direccion 1":val.get("linea_direccion1"),
                "Direccion 2":val.get("linea_direccion2")
            })
    return direccion   
def menu():
    while True:
     print("""
REPORTES DE LAS OFICINAS
0. Regresar al menu principal
1. Obtener los codigos de las todas oficinas y las ciudades de ubicacion
2. Obtener el telefono de todas las oficinas del pais ingresado
3. Obtener las direcciones de todas las oficinas
""")
     op=int(input("Seleccione una de las opciones: "))
     if(op==1):
        print(tabulate(getAllCodigoCiudad(),headers="keys",tablefmt="grid"))
     elif(op==2):
        try:
            pais=input("Ingrese el pais con mayuscula(s) inicial(es): ")
            print(tabulate(getAllCiudadTelefono(pais),headers="keys",tablefmt="grid"))
        except KeyboardInterrupt:
            return menu()
     elif(op==3):
        print(tabulate(getAllDirecciones(),headers="keys",tablefmt="grid"))
     elif (op==0):
        break